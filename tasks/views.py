from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


from tasks.serializers import RegisterSerializer, TaskSerializer, TagSerializer


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(APIView):
    def get(self, request):
        tasks = Task.objects.filter(user__id=request.user.id)

        is_done = request.query_params.get('is_done')
        if is_done:
            tasks = tasks.filter(is_done=is_done)

        priority = request.query_params.get('priority')
        if priority:
            tasks = tasks.filter(priority=priority)

        tag = request.query_params.get('tag')
        if tag:
            tasks = tasks.filter(tag=tag)

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TaskDetailView(APIView):
    def _return_task_model(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        if task.user.id != request.user.id:
            return None
        return task

    def get(self, request, pk):
        task = self._return_task_model(request, pk)
        if task is None: return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = self._return_task_model(request, pk)
        if task is None: return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self._return_task_model(request, pk)
        if task is None: return Response(status=status.HTTP_403_FORBIDDEN)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class AllTasksListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        print(tasks.query)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagListCreateView(APIView):
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)