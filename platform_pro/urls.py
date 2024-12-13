from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('platform_app.urls')),
    path('idea/', include('idea_block.urls')),
    path('polls_qna/', include('polls_qna.urls')),
    path('prize_system/', include('prize_system.urls')),
]
