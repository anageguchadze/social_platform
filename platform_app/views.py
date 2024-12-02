from rest_framework import viewsets
from .models import *
from .serializers import *


class CustomUserViewSet(viewsets.ModelViewSet):
    #apiview
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

#register
#login
#logout

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ForumTopicsViesWet(viewsets.ModelViewSet):
    queryset = ForumTopics.objects.all()
    serializer_class = ForumTopicsSerializer

class ForumMessageViewSet(viewsets.ModelViewSet):
    queryset = ForumMessages.objects.all()
    serializer_class = ForumMessagesSerializer