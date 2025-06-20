from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import *
from .serializers import *


class TaskList(APIView):
    def get(self, request, format=None):
        tasks = Task.objects.all().order_by('-created_at')
        serializer = Taskserializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Taskserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = Taskserializer(task)
        return Response(serializer.data)

    def put(self, request, format=None):
        task = self.get_object(pk)
        # Если ты хочешь не просто посмотреть на объект,
        # а обновить его данными из запроса
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self,get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


