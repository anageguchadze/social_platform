from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

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


    # def save(self,*args, **kwargs):
    #     self.points = 


class Category(models.Model):
    category = models.CharField(max_length=255)
    

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

