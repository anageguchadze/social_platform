from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)


router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'forumtopics', ForumTopicsViewSet)
router.register(r'forummessages', ForumMessageViewSet)


urlpatterns =[
    path('', include(router.urls)),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('auth/register/', RegistrationView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('register-device/', RegisterDeviceView.as_view(), name='register_device'),
    path('send-notification/', SendNotificationView.as_view(), name='send_notification'),
]
