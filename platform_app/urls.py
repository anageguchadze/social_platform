from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'forumtopics', ForumTopicsViesWet)
router.register(r'forummessages', ForumMessageViewSet)


urlpatterns =[
    path('api/', include(router.urls)),
    
]