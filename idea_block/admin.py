from django.contrib import admin
from .models import Idea, Vote


admin.site.register(Idea)
admin.site.register(Vote)