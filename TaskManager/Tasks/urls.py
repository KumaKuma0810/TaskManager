from .views import *

urlpatterns = [
    path('task/all', TaskList.as_veiw(), name='task_all'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
]
