from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from account.models import User, ParentConnect
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = '__all__'
        # fields = ['email']


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email']


# class UserProfileAPIView(APIView):
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         user = request.user
#         user_profile = User.objects.get(user=user)
#         serializer = self.serializer_class(user_profile)
#         return Response({"success": True, "status": "Success", "data": serializer.data}, status=status.HTTP_201_CREATED)

# class CurrentUserView(APIView):
#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)

    # tokens = serializers.SerializerMethodField()
    tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

    # def get_tokens(self, obj):
    #     user = User.objects.get(email=obj['email'])
    #
    #     return {
    #         'refresh': user.tokens()['refresh'],
    #         'access': user.tokens()['access']
    #     }

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        username = attrs.get('username', '')
        # filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        # if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
        #     raise AuthenticationFailed(
        #         detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)


class CurrentUserSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=255, min_length=3)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class InviteParentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)

    class Meta:
        model = User
        fields = '__all__'


class ParentConnectSerializer(serializers.ModelSerializer):
    student = UserSerializer()

    # parent = UserSerializer()

    class Meta:
        model = ParentConnect
        fields = '__all__'
