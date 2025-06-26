from .views import *
from django.urls import path

# TokenObtainPairView - обработчик для получения пары токенов (access и refresh) при логине.
# TokenRefreshView - обработчик для обновления access-токена с помощью refresh-токена.
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('task/all', TaskList.as_view(), name='task_all'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

]
