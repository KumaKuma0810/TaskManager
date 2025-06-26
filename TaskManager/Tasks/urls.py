from .views import *
from django.urls import path


urlpatterns = [
    path('task/all', TaskList.as_view(), name='task_all'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
]
