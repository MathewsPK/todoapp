from django.contrib import admin
from django.urls import path
from.import views
from .views import home, tasks, update_task, delete_task

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', tasks, name='tasks'),
    path('tasks/update/<int:task_id>/', update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('admin/', admin.site.urls),
]
