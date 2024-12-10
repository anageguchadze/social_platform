from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Idea, Vote


class IdeaSerializer(serializers.ModelSerializer):
    """
    Serializer for Idea model.
    Includes the submitter's username.
    """
    submitted_by = serializers.StringRelatedField(read_only=True)  # Show username, but don't allow to edit.
    
    class Meta:
        model = Idea
        fields = ['id', 'title', 'description', 'submitted_by', 'created_at']


class VoteSerializer(serializers.ModelSerializer):
    """
    Serializer for Vote model.
    Allows submitting votes with validation.
    """
    user = serializers.StringRelatedField(read_only=True)  # Prevent unauthorized changes
    idea = serializers.PrimaryKeyRelatedField(queryset=Idea.objects.all())

    class Meta:
        model = Vote
        fields = ['id', 'user', 'idea', 'vote_type', 'created_at']
