from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from push_notifications.models import GCMDevice


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
        ('guest/intern', 'Guest/Intern')
    )

    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    points = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    interests = models.TextField(blank=True, null=True)  # New field for user interests

    def __str__(self):
        return self.username



class Category(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.TextField(default="No description")
    is_active = models.BooleanField(default=True)  # კატეგორიის აქტიურობის მდგომარეობა

    def __str__(self):
        return self.category_name

    

class ForumTopics(models.Model):
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    topic_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topic_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class ForumMessages(models.Model):
    message_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(ForumTopics, on_delete=models.CASCADE)
    parent_message = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def upvote(self):
        self.upvotes += 1
        self.save()

    def downvote(self):
        self.downvotes += 1
        self.save()

    def get_total_votes(self):
        return self.upvotes - self.downvotes


def register_device(user, registration_id):
    device, created = GCMDevice.objects.get_or_create(user=user)
    device.registration_id = registration_id
    device.save()
    return device

def send_notification(user, message):
    try:
        # მომხმარებლის რეგისტრირებული მოწყობილობის შეზღუდვა
        device = GCMDevice.objects.get(user=user)  # დაამოწვე, არსებობს თუ არა
        # Push შეტყობინების გაგზავნა
        device.send_message(message)
        return True
    except GCMDevice.DoesNotExist:
        return False  # არ არსებობს მოწყობილობა