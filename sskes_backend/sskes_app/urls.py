from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from sskes_app import views
from account.views import user_api
from sskes_app.views import get_courses, create_course, create_lesson, get_lesson, get_enrollments, get_all_courses, create_enrollments, course_publish,save_answer,complete_course,doing_course

urlpatterns = [
                  # path('api/v1/', include('djoser.urls')),
                  path('api/v1/courseRegister/', create_course),
                  path('api/v1/getCourses/', views.get_courses),
                  path('api/v1/lessonRegister/', create_lesson),
                  path('api/v1/getLessons/', get_lesson),
                  path('api/v1/getEnrollments/', get_enrollments),
                  path('api/v1/createEnrollments/', create_enrollments),
                  path('api/v1/get_all_courses/', get_all_courses),
                  path('api/v1/pubCourse/', course_publish),
                  path('api/v1/saveAnswer/', save_answer),
                  path('api/v1/completeCourse/', complete_course),
                  path('api/v1/notcompleteCourse/', doing_course),
              ]
