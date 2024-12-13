from django.db.models.signals import post_save
from django.dispatch import receiver
from platform_app.models import ForumMessages, ForumTopics
from idea_block.models import Idea
from polls_qna.models import Answer
from prize_system.models import UserActivity


@receiver(post_save, sender=ForumMessages)
def award_points_for_post(sender, instance, created, **kwargs):
    if created:
        UserActivity.award_points(instance.message_user, 'post_created', points=10)


@receiver(post_save, sender=Idea)
def award_points_for_idea(sender, instance, created, **kwargs):
    if created:
        UserActivity.award_points(instance.submitted_by, 'idea_shared', points=20)


@receiver(post_save, sender=Answer)
def award_points_for_answer(sender, instance, created, **kwargs):
    if created:
        UserActivity.award_points(instance.created_by, 'question_answered', points=15)
