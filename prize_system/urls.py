from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserActivityViewSet


router = DefaultRouter()
router.register(r'activities', UserActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
