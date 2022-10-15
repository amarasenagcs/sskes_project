from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Course, Lesson, Enrollment, User
from account.serializers import UserSerializer


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'grade', 'short_description', 'get_image')


class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'lesson_name', 'content_description', 'course', 'content_type', 'get_content')


class EnrollmentsDetailSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer()
    student = UserSerializer()
    teacher = UserSerializer()

    class Meta:
        model = Enrollment
        fields = '__all__'


class CreateEnrollment(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'


class CreateLesson(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CompleteCoursesSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer()

    class Meta:
        model = Enrollment
        fields = '__all__'
