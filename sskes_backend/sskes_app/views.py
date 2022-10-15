from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import serializers, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.
from account.serializers import UserSerializer
from rest_framework.utils import json
from rest_framework.utils.encoders import JSONEncoder

from .models import Course, Lesson, Enrollment, User
from .serializer import CourseDetailSerializer, LessonDetailSerializer, EnrollmentsDetailSerializer, CreateEnrollment, \
    CreateLesson, CreateCourseSerializer, CompleteCoursesSerializer
from account.permissions import IsAuthor
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.forms.models import model_to_dict
from django.db.models import Q


@api_view(['GET'])
def get_courses(request):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    courses = Course.objects.filter(teacher_id=request.user.id)
    serializer = CourseDetailSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_courses(request):
    courses = Course.objects.filter(status='publish')
    serializer = CourseDetailSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def create_course(request):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)

    serializer = CreateCourseSerializer(data=request.data, partial=True)
    print(request.data)

    if serializer.is_valid(raise_exception=True):
        user = request.user.id
        serializer.save(teacher_id=user)
    return Response(serializer.data)


@api_view(['GET'])
def get_lesson(request):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    course = request.query_params.get('courseId')
    # print(course)
    lessons = Lesson.objects.filter(course_id=course)
    serializer = LessonDetailSerializer(lessons, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_answer(request):
    coursId = request.data['courseId']
    file = request.data['file']
    enrolment = Enrollment.objects.filter(course=coursId).filter(student=request.user)
    enrolment[0].answer = file
    enrolment[0].save()


@api_view(['GET'])
def complete_course(request):
    user = request.user
    # file = request.data['file']
    # Entry.objects.filter(~Q(id=3))
    enrolment = Enrollment.objects.filter(~Q(grade='none')).filter(student=user)
    serializer = CompleteCoursesSerializer(enrolment, many=True)
    return Response({"completeCourse": serializer.data})

@api_view(['GET'])
def doing_course(request):
    user = request.user
    # file = request.data['file']
    # Entry.objects.filter(~Q(id=3))
    enrolment = Enrollment.objects.filter(grade='none').filter(student=user)
    serializer = CompleteCoursesSerializer(enrolment, many=True)
    return Response({"notCompleteCourse": serializer.data})


@api_view(['GET'])
def course_publish(request):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    course = request.query_params.get('courseId')
    # print(course)
    getCourse = Course.objects.get(id=course)
    print(getCourse.status)
    if getCourse.status == 'publish':
        return Response({'error': 'Already publish'})
    else:
        getCourse.status = 'publish'
        getCourse.save()
        return Response({'status': 'publish successfully'})


@api_view(['POST'])
@permission_classes([AllowAny])
def create_lesson(request):
    serializer = CreateLesson(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.to_json()


@api_view(['GET'])
def get_enrollments(request):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    # enrollments = Enrollment.objects.filter(teacher_id=request.user.id).values_list('student_id')
    # courses = Course.objects.filter(teacher_id=request.user.id).values_list('id')
    # std = Enrollment.objects.filter(course__in=courses).values_list('student_id')
    # user = User.objects.filter(id__in=std).values_list('first_name')
    # enrollInfo = User.objects.filter(Q(groups__name='resolver') | Q(groups__name='admin'))
    # std = User.objects.filter(id__in=enrollments.id)

    courses = Course.objects.filter(teacher_id=request.user.id)
    std = Enrollment.objects.filter(course__in=courses)
    serializer = EnrollmentsDetailSerializer(std, many=True)
    print(std)
    # x = json.dumps(std, cls=MyJSONEncoder)
    return Response({"enrollment": serializer.data})
    # return JsonResponse( model_to_dict(std))
    # enrollInfo = User.objects.filter(Q(groups_name='resolver') | Q(groups_name='admin'))
    # std = User.objects.filter(id__in=enrollments.id)
    # print(std)
    # for i in std:
    #     print(i.course.title)
    # studInfo = []
    # for e in enrollments:
    #     std = User.objects.get(id=e.id)
    #     studInfo.append(std)
    #     print(std.first_name)
    # print(studInfo)
    # queryset = User.objects.filter(
    #     id=enrollments[1].student_id
    # ).values('first_name')
    # print(list(queryset.values('first_name')))
    # return list(queryset.values('first_name'))

    # return Response(serializer.data)


@api_view(['GET'])
def create_enrollments(request):
    # serializer = CreateEnrollment(data=request.data)
    # course_id = request.query_params['course']
    course_id = request.query_params['course']
    user_id = request.user
    x = Enrollment.objects.filter(course_id=course_id).filter(student=user_id)
    if x.count() == 1:

        # for i in x:
        print("Condition working")
        return Response({'status': 'error'})
    else:
        print("Else Condition working")
        print(course_id)
        teacher = Course.objects.get(id=course_id)
        teacher_id = teacher.teacher
        print(teacher_id)
        Enrollment.objects.create(course_id=course_id, teacher=teacher_id, student=user_id)
        return Response({'status': 'success'})
    # if serializer.is_valid(raise_exception=True):
    #     serializer.save(student=request.user.id, course=course_id.teacher.id)
    # return Response(serializer.data)
