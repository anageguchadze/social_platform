from django.db import models
from django.conf import settings

class UserActivity(models.Model):
    """
    Represents a single activity performed by a user and the points earned for it.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="activities"
    )
    activity_type = models.CharField(max_length=50, choices=[
        ('post_created', 'Post Created'),
        ('idea_shared', 'Idea Shared'),
        ('question_answered', 'Question Answered'),
    ])
    points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} earned {self.points} points for {self.activity_type}"

    @staticmethod
    def award_points(user, activity_type, points):
        """
        A helper method to record points for a user's activity.
        """
        UserActivity.objects.create(user=user, activity_type=activity_type, points=points)
        user.points += points
        user.save()

