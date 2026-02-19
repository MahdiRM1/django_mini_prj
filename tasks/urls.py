from django.urls import path
from tasks.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('tasks/all/', AllTasksListView.as_view()),
    path('tasks/', TaskListCreateView.as_view()),
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('tags/', TagListCreateView.as_view()),
]