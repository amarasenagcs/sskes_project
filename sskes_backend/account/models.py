from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "http://localhost:8080" + "{}?token={}".format(
        reverse('password_reset:reset-password-request'),
        reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="SSKES Account"),
        # message:
        email_plaintext_message,
        # from:
        "testingproject4us@gmail.com",
        # to:
        [reset_password_token.user.email]
    )


# Create your models here.

# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#
#         if username is None:
#             raise TypeError('Users should have a username')
#         if email is None:
#             raise TypeError('Users should have a email')
#         user = self.model(username=username, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()


class User(AbstractUser):
    # username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    updated_at = models.DateField(auto_now_add=True)
    is_admin = models.BooleanField('Is admin', default=False)
    is_teacher = models.BooleanField('Is teacher', default=False)
    is_parent = models.BooleanField('Is parent', default=False)
    is_student = models.BooleanField('Is student', default=False)
    is_verified = models.BooleanField('Is verified', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class ParentConnect(models.Model):
    accept = 'accept'
    reject = 'reject'
    pending = 'pending'

    CHOICES_TYPE = (
        (accept, 'accept'),
        (reject, 'reject'),
        (pending, 'pending')
    )

    created_at = models.DateField(auto_now_add=True)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.OneToOneField(User, related_name="parent_student", on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default=pending, choices=CHOICES_TYPE)
