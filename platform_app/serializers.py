from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'role', 'password']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ForumTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumTopics
        fields = '__all__'

class ForumMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumMessages
        fields = '__all__'