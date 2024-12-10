from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Idea, Vote
from .serializers import IdeaSerializer, VoteSerializer


class IdeaViewSet(viewsets.ModelViewSet):
    """
    Handles logic related to Idea model.
    Allows listing, creating, and retrieving ideas.
    """
    serializer_class = IdeaSerializer
    queryset = Idea.objects.all().order_by('-created_at')
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically associate the idea submission with the logged-in user
        serializer.save(submitted_by=self.request.user)


class VoteViewSet(viewsets.ViewSet):
    """
    Handles logic related to voting on ideas.
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """
        Handle creating a vote (upvote/downvote).
        """
        serializer = VoteSerializer(data=request.data)
        if serializer.is_valid():
            # Check if the user has already voted
            idea_id = serializer.validated_data['idea'].id
            user_id = request.user.id
            vote, created = Vote.objects.get_or_create(
                user=request.user,
                idea_id=idea_id,
                defaults={'vote_type': serializer.validated_data['vote_type']}
            )
            if not created:
                # If user has already voted, update their vote type
                vote.vote_type = serializer.validated_data['vote_type']
                vote.save()
            
            return Response({"message": "Vote added/updated successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
