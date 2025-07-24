from django.utils import timezone
from rest_framework import generics, serializers
from task.models import Task, Log
from task.serializers import TaskSerializer


class TaskCreateApiView(generics.CreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer: serializers.BaseSerializer) -> None:
        instance = serializer.save()
        check_date(instance)
        Log.objects.create(
            task=instance,
            text='Создание записи'
        )


class TaskDestroyAPIView(generics.DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_destroy(self, instance):
        Log.objects.create(
            text=f'Удаление записи c ID={instance.id}'
        )
        instance.delete()


class TaskUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_update(self, serializer: serializers.BaseSerializer) -> None:
        instance = serializer.save()
        check_date(instance)
        Log.objects.create(
            task=instance,
            text=f'Изменение записи'
        )


class TaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


def check_date(instance):
    """
    Проверка даты начала и окончания задачи
    """
    message = None
    if instance.start < timezone.now():
        message = 'Дата начала раньше текущего времени'
    elif instance.deadline < instance.start:
        message = 'Дата окончания раньше даты начала'

    if message:
        Log.objects.create(
            task=instance,
            text=message
        )
        raise ValueError(message)
