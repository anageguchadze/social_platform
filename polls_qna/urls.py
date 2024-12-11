from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet, QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename="poll")
router.register(r'questions', QuestionViewSet, basename="question")
router.register(r'answers', AnswerViewSet, basename="answer")

urlpatterns = [
    path('', include(router.urls)),
]
