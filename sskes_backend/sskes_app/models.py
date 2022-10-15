from django.core.validators import FileExtensionValidator
from django.db import models
from io import BytesIO
from django.core.files import File

# Create your models here.
from account.models import User


class Course(models.Model):
    # categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    subject = models.CharField(max_length=50, blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='course_assets/')
    status = models.CharField(max_length=20, default='draft')

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Lesson(models.Model):
    video = 'video'
    article = 'article'
    assignment = 'assignment'

    CHOICES_TYPE = (
        (video, 'video'),
        (article, 'article'),
        (assignment, 'assignment')
    )

    lesson_name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=20, choices=CHOICES_TYPE, default=assignment)
    content_description = models.TextField(blank=True, null=True)
    content = models.FileField(upload_to='lesson_assets/', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def get_content(self):
        if self.content:
            return 'http://127.0.0.1:8000' + self.content.url
        return ''


class Enrollment(models.Model):
    created_at = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="student_enrollment", on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now_add=True)
    answer = models.FileField(upload_to='answers/', null=True, blank=True)
    grade = models.CharField(max_length=20, default='none')

