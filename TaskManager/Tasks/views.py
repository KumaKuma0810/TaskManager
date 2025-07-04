from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generic


from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Task
from .serializers import TaskSerializers


class RegisterView(generics.CreateAPIView):
    # реализует логику POST-запроса для создания объекта.
    queryset = User.objects.all()
    # Обязательное поле, чтобы DRF знал, с чем работает view.
    serializer_class = RegisterSerializer


class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks = Task.objects.filter(user=request.user).order_by('-created_at')
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializers(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
