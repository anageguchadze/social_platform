from rest_framework import viewsets
from .models import UserActivity
from .serializers import UserActivitySerializer


class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = UserActivity.objects.all().order_by('-created_at')
    serializer_class = UserActivitySerializer
