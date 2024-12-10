from django.db import models
from django.conf import settings


class Idea(models.Model):
    """
    Represents an idea submitted by an employee.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ideas"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Vote(models.Model):
    """
    Represents a vote by a user on an idea.
    """
    UPVOTE = 1
    DOWNVOTE = -1

    VOTE_CHOICES = [
        (UPVOTE, "Upvote"),
        (DOWNVOTE, "Downvote"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes"
    )
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="votes")
    vote_type = models.IntegerField(choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'idea')  # Prevent multiple votes by same user on the same idea.

    def __str__(self):
        return f"{self.user.username} voted {self.vote_type} on {self.idea.title}"
