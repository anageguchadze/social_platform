from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Poll, PollOption, PollResponse, Question, Answer
from .serializers import PollSerializer, PollResponseSerializer, QuestionSerializer, AnswerSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all().order_by('-created_at')
    serializer_class = PollSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def respond(self, request, pk=None):
        """Handle poll responses."""
        poll = self.get_object()
        option_id = request.data.get('option_id')

        try:
            option = PollOption.objects.get(id=option_id, poll=poll)
            response, created = PollResponse.objects.get_or_create(
                user=request.user,
                poll=poll,
                defaults={'option': option}
            )
            if not created:
                response.option = option
                response.save()
            return Response({"message": "Response recorded."}, status=status.HTTP_200_OK)
        except PollOption.DoesNotExist:
            return Response({"error": "Invalid option."}, status=status.HTTP_400_BAD_REQUEST)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-created_at')
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-created_at')
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
