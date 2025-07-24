from django.urls import path
from task.views import TaskCreateApiView, TaskDestroyAPIView, TaskUpdateAPIView, TaskListAPIView
from task.apps import TaskConfig

app_name = TaskConfig.name

urlpatterns = [
    path("create/", TaskCreateApiView.as_view(), name="create"),
    path("<int:pk>/delete/", TaskDestroyAPIView.as_view(), name="delete"),
    path("<int:pk>/update/", TaskUpdateAPIView.as_view(), name="update"),
    path("list/", TaskListAPIView.as_view(), name="list"),
]
