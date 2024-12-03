from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'profile_picture', 'bio', 'points']


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