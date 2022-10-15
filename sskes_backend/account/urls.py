from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.views import login_api, register_api, home_api, user_api, current_user, VerifyEmail, LoginAPIView, ParentConnectReq, \
    get_std_parent, save_std_response,get_children, remove_children
# from sskes_backend.account.views import
# from sskes_backend.account.views import otp_verification
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
router = DefaultRouter()
# router.register('User')

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1', include('djoser.urls.authtoken')),
    path('api/v1/email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('api/v1/login/', login_api),
    # path('api/v1/login/', LoginAPIView.as_view(), name="login"),
    path('api/v1/registerUser/', register_api),
    path('api/v1/home/', home_api),
    path('api/v1/getUser/', user_api),
    path('api/v1/getCurrentUser/', current_user),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/v1/sendInvitationParent/', ParentConnectReq),
    path('api/v1/getInvitationParent/', get_std_parent),
    path('api/v1/resInvitationParent/', save_std_response),
    path('api/v1/getParentChildren/', get_children),
    path('api/v1/remParentChildren/', remove_children),
    # path('api/v1/testing/', test),

]
