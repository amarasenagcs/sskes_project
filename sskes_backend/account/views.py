import requests
from django.shortcuts import render
from datetime import date
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Exists, OuterRef
from rest_framework import serializers, status, generics
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
import jwt
from rest_framework_simplejwt.tokens import RefreshToken

from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

from account.models import User
from account.models import ParentConnect
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, EmailSerializer, LoginSerializer, CurrentUserSerializer, \
    InviteParentSerializer, ParentConnectSerializer
from django.urls import reverse
from rest_framework import permissions
from .permissions import IsAuthor
from django.shortcuts import render
import random
import string

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from sskes_app.models import Course
from account.models import ParentConnect


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    form = AuthenticationForm(request, request.data)
    user_name = request.data.get('username', None)
    if not form.is_valid():
        raise serializers.ValidationError(form.errors)
    user = User.objects.get(username=user_name)
    login(request, form.get_user())
    user_details = User.objects.filter(username=user_name)
    serializer = LoginSerializer(user_details, many=True)
    accesstoken = RefreshToken.for_user(user).access_token

    if not user.is_verified:
        return Response({'error': 'Please activate you account'}, status=status.HTTP_400_BAD_REQUEST)

    if user.is_parent:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'userType': 'parent', 'accessToken': str(accesstoken), 'username': user_name,
             'userDetails': serializer.data},
            status=HTTP_200_OK)
        # return Response("parent")
    elif user.is_teacher:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'userType': 'teacher', 'accessToken': str(accesstoken), 'username': user_name,
             'userDetails': serializer.data},
            status=HTTP_200_OK)
        # return Response("teacher")
    elif user.is_student:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'userType': 'student', 'accessToken': str(accesstoken), 'username': user_name,
             'userDetails': serializer.data},
            status=HTTP_200_OK)
        # return Response("student")
    else:
        return Response("error")


@api_view()
def logout_api(request):
    logout(request)
    return Response()


# def create_unique_id():
#     return ''.join(random.choices(string.digits, k=8))


# @api_view(['POST'])
# def register_api(request):
# serializer = EmailSerializer(data=request.data)
# if serializer.is_valid(raise_exception=True):
# request.session.set_expiry(300)
# otp = create_unique_id()
# request.session['otp'] = otp
# print("the otp is : " + request.session['otp'])
# user_data = serializer.data
# user = user_data['email']
# absurl = 'This is your otp code : ' + str(otp)
# email_body = 'Hi ' + user + \
#              ' Use this one time password to verify your email \n' + absurl
# data = {'email_body': email_body, 'to_email': user,
#         'email_subject': 'Verify your email'}
#
# Util.send_email(data)
# return Response(user_data, status=status.HTTP_201_CREATED)
# request.session['user_data'] = serializer
# serializer.save()
# user_data = serializer.data
# user = User.objects.get(email=user_data['email'])
# token = RefreshToken.for_user(user).access_token
# print("this is the token :" + str(token))
# current_site = get_current_site(request).domain
# relativeLink = reverse('email-verify')
# absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
# email_body = 'Hi ' + user.username + \
#              ' Use the link below to verify your email \n' + absurl
# data = {'email_body': email_body, 'to_email': user.email,
#         'email_subject': 'Verify your email'}

# Util.send_email(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_api(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    user_data = serializer.data
    user = User.objects.get(email=user_data['email'])
    token = RefreshToken.for_user(user).access_token
    print("this is the token :" + str(token))
    current_site = '127.0.0.1:8000'
    relativeLink = reverse('email-verify')
    absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
    email_body = 'Hi ' + user.username + \
                 ' Use the link below to verify your email \n' + absurl
    data = {'email_body': email_body, 'to_email': user.email,
            'email_subject': 'Verify your email'}

    Util.send_email(data)
    return Response(user_data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def home_api(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def user_api(request):
    # form = AuthenticationForm(request, request.data)
    # print('hi', request.data)
    # return Response(request.data)
    username = request.data.get('username', None)
    user = User.objects.filter(username=username)
    print('this ', user)
    # # user = User.objects.get(username=user_name)
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def current_user(request):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    serializer = CurrentUserSerializer(request.user)
    CourseCount = Course.objects.filter(teacher_id=request.user.id).count()
    print('this ', request.user.first_name)
    return Response({'userInfo': serializer.data, 'CourseCount': CourseCount})


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        print("this is the received token :" + str(token))
        try:
            # print("hi user" )
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            # print("this is the user id :" + str(user))
            if not user.is_verified:
                user.is_verified = True
                # serializer = request.session['user_data']
                # serializer.save()
                user.save()
            return Response({'email': 'Successfully Activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


# def create_unique_id():
#     return ''.join(random.choices(string.digits, k=8))
#
#
# @api_view(['POST'])
# def VerifyEmail(request):
#     serializer = EmailSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     # if serializer.is_valid(raise_exception=True):
#     #     serializer.save()
#     user_data = serializer.data
#     # user = User.objects.get(email=user_data['email'])
#     user = user_data['email']
#     otp = create_unique_id()
#     request.session['otp'] = otp
#     request.session.set_expiry(300)
#     print("the otp is : "+request.session['otp'])
#     absurl = 'This is your otp code : ' + str(otp)
#     email_body = 'Hi ' + user + \
#                  ' Use this one time password to verify your email \n' + absurl
#     data = {'email_body': email_body, 'to_email': user,
#             'email_subject': 'Verify your email'}
#
#     Util.send_email(data)
#     return Response(user_data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def otp_verification(request):
#     otp = request.data['otp']
#     print("this is the user otp : " + str(otp))
# request.session.keys()
# print("this is the session otp : " + request.session['otp'])
# request.session.get('prop_name')
# print("this session otp : " + str(request.session.get('otp')))
# if int(otp) == int(request.session['otp']):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response({'result': 'Successfully Activated', 'status': True}, status=status.HTTP_200_OK)
#     print("otp successfully match")
#
# else:
#     print("otp invalid!")
#     return Response({'error': 'otp invalid!', 'status': False}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# class ParentConnect(generics.GenericAPIView):
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user_data = serializer.data
#             user = User.objects.get(email=user_data['email'])
#             student = User.objects.filter(is_student=True).filter(user=user)
#             print(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def ParentConnectReq(request):
    permission_classes = (permissions.IsAuthenticated, IsAuthor)
    email = request.data['email']
    # print("email is :" + str(email))

    # serializer_class = ParentConnectSerializer
    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        if user.is_student == True:
            student = ParentConnect.objects.filter(parent=request.user).filter(student=user)
            parent = request.user

            if student.count() == 1:
                if student[0].status == 'pending':
                    return Response({'error': 'already requested!'})
            else:
                ParentConnect.objects.create(student=user, parent=parent)
                return Response({'success': 'successfully invite!'})
        else:
            return Response({'error': 'user does not student'})
    else:
        return Response({'error': 'user does not exists'})


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def get_std_parent(request):
    # permission_classes = (permissions.IsAuthenticated, IsAuthor)
    currentUser = request.user
    if ParentConnect.objects.filter(student=currentUser).exists():
        std = ParentConnect.objects.get(student=currentUser)
        if std.status == 'pending':
            return Response({'status': 'pending', 'parent': std.parent.first_name, 'parentConId': std.id})
        else:
            return Response({'status': 'accept or reject'})
    else:
        return Response({'error': 'user have not request'})
    # serializer = ParentConnectSerializer(parent=request.user.id, many=True)
    # parnetReqCount = ParentConnect.objects.filter(teacher_id=request.user.id).count()
    # print('this ', request.user.first_name)
    # return Response({'userInfo': ''})


@api_view(['POST'])
def save_std_response(request):
    # response = request.data
    userId = request.user
    print(request.data['status'])
    if request.data['status'] == 'confirm':
        getPt = ParentConnect.objects.get(id=request.data['parentConId'])
        getPt.status = 'accept'
        getPt.save()
        return Response({'status': 'accept successfully'})
    if request.data['status'] == 'reject':
        getPt = ParentConnect.objects.get(id=request.data['parentConId'])
        getPt.status = 'reject'
        getPt.save()
        return Response({'status': 'reject successfully'})


@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def get_children(request):
    parent = request.user
    print(parent)
    childrens = ParentConnect.objects.filter(parent=parent).filter(status='accept')
    print(childrens)

    students = ParentConnectSerializer(childrens, many=True)
    # students.is_valid(raise_exception=True)
    return Response(students.data)

@api_view(['POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
def remove_children(request):
    parntConId= request.data['parntConId']
    print(parntConId)
    # parent = request.user
    ParentConnect.objects.filter(id=parntConId).delete()
    # students.is_valid(raise_exception=True)
    return Response({'status': 'delete successfully'})
