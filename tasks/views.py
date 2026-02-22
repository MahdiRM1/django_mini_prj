from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwner
from .models import *

from tasks.serializers import RegisterSerializer, TaskSerializer, TagSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AllTasksListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer