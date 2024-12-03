from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from .models import *
from .serializers import *


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Token blacklisted successfully!"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token or token already blacklisted."}, status=status.HTTP_400_BAD_REQUEST)


class CustomUserViewSet(viewsets.ModelViewSet):
    #apiview
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

#register
#login
#logout

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ForumTopicsViesWet(viewsets.ModelViewSet):
    queryset = ForumTopics.objects.all()
    serializer_class = ForumTopicsSerializer

class ForumMessageViewSet(viewsets.ModelViewSet):
    queryset = ForumMessages.objects.all()
    serializer_class = ForumMessagesSerializer


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]