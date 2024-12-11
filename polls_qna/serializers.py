from rest_framework import serializers
from .models import Poll, PollOption, PollResponse, Question, Answer


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = ['id', 'option_text']


class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'created_by', 'created_at', 'is_active', 'options']


class PollResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollResponse
        fields = ['id', 'user', 'poll', 'option']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'created_by', 'created_at']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'content', 'created_by', 'created_at']
