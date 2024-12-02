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

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # points = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, null=True)
    