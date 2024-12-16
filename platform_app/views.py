from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from .models import *
from .serializers import *
from push_notifications.models import GCMDevice
from django.contrib.auth import get_user_model
from idea_block.models import Idea
from polls_qna.models import Answer

User = get_user_model()

class RegisterDeviceView(APIView):
    """
    დარეგისტრირეთ Firebase Token GCMDevice-თან.
    """
    def post(self, request):
        user_id = request.data.get('user_id')
        registration_id = request.data.get('registration_id')

        if not user_id or not registration_id:
            return Response({"error": "Missing user_id or registration_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)  # მომხმარებელი გაამოწვოს
            # რეგისტრაცია GCMDevice-ის
            device, created = GCMDevice.objects.get_or_create(user=user)
            device.registration_id = registration_id
            device.save()
            return Response({"message": "Device registered successfully"}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class UserActivityHistoryView(APIView):
    """
    View a user's activity history: posts, ideas, answers.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)

        posts = ForumMessages.objects.filter(message_user=user).values('id', 'message_body', 'timestamp')
        ideas = Idea.objects.filter(submitted_by=user).values('id', 'title', 'created_at')
        answers = Answer.objects.filter(created_by=user).values('id', 'content', 'created_at')

        return Response({
            "user": user.username,
            "posts": list(posts),
            "ideas": list(ideas),
            "answers": list(answers)
        })


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


class UserProfileView(generics.RetrieveAPIView):
    """
    View a user's profile.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileEditView(generics.UpdateAPIView):
    """
    Edit the logged-in user's profile.
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ForumTopicsViewSet(viewsets.ModelViewSet):
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


class ForumTopicVote(APIView):
    def post(self, request, topic_id):
        try:
            topic = ForumTopics.objects.get(id=topic_id)
            action = request.data.get('action')
        
            if action == 'upvote':
                topic.upvote()
            elif action == 'downvote':
                topic.downvote()
            
            return Response({"message": "Vote registered successfully!"}, status=status.HTTP_200_OK)
        except ForumTopics.DoesNotExist:
            return Response({"error": "Topic not found"}, status=status.HTTP_404_NOT_FOUND)


class ForumMessageVote(APIView):
    def post(self, request, message_id):
        message = ForumMessages.objects.get(id=message_id)
        action = request.data.get('action')
        
        if action == 'upvote':
            message.upvote()
        elif action == 'downvote':
            message.downvote()
        
        return Response({"message": "Vote registered successfully!"}, status=status.HTTP_200_OK)
    

class ForumTopicCreate(APIView):
    def post(self, request):
        title = request.data.get('title')
        category_id = request.data.get('category_id')
        topic_category = Category.objects.get(id=category_id)
        topic_author = request.user
        
        topic = ForumTopics.objects.create(
            title=title,
            topic_category=topic_category,
            topic_author=topic_author
        )
        
        return Response({"message": "Topic created successfully!"}, status=status.HTTP_201_CREATED)

class ForumMessageCreate(APIView):
    def post(self, request):
        message_body = request.data.get('message_body')
        topic_id = request.data.get('topic_id')
        topic = ForumTopics.objects.get(id=topic_id)
        message_user = request.user
        
        message = ForumMessages.objects.create(
            message_user=message_user,
            message_body=message_body,
            topic=topic
        )
        
        return Response({"message": "Message created successfully!"}, status=status.HTTP_201_CREATED)

    
class SendNotificationView(APIView):
    """
    Push შეტყობინებების გაგზავნა GCMDevice-ის საშუალებით.
    """
    def post(self, request):
        user_id = request.data.get('user_id')
        message = request.data.get('message')

        if not user_id or not message:
            return Response({"error": "Missing user_id or message"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
            devices = GCMDevice.objects.filter(user=user)  # ჩამოთვლა ყველა რეგისტრირებული მოწყობილობა
            if devices.exists():
                for device in devices:
                    device.send_message(message)
                return Response({"message": "Notification sent successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "User device not found!"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User does not exist!"}, status=status.HTTP_404_NOT_FOUND)
