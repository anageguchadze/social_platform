from django.contrib import admin
from .models import Poll, PollOption, PollResponse, Question, Answer

# Register your models here.
admin.site.register(Poll)
admin.site.register(PollOption)
admin.site.register(PollResponse)
admin.site.register(Question)
admin.site.register(Answer)