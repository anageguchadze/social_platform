from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import *


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)  # Use a more descriptive field name

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'confirm_password', 'role']
        extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}

    def validate(self, data):
        """
        Validate that the password and confirm_password fields match.
        """
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return data

    def create(self, validated_data):
        # Remove the confirm_password field as it isn't needed for saving the user
        validated_data.pop('confirm_password')

        # Hash the password before saving it
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    
        

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role', 'profile_picture', 'bio', 'points']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'interests', 'profile_picture', 'points']
        read_only_fields = ['id', 'username', 'email', 'points']
        

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