from django.contrib import admin

# Register your models here.
from sskes_app.models import Course,Lesson, Enrollment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Enrollment)