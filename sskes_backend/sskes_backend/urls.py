from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import authtoken

from account.views import home_api, login_api, register_api, current_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('sskes_app.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('', include('rest_framework.urls')),
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
