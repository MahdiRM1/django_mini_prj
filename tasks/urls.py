from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

tags_router = DefaultRouter()
tags_router.register(r'tags', TagViewSet)

urlpatterns = [
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('tasks/all/', AllTasksListView.as_view()),
    path('tasks/', TaskListCreateView.as_view()),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('', include(tags_router.urls)),
]