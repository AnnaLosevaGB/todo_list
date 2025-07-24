from django.db import models
from django.utils.timezone import now


class Task(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание')
    deadline = models.DateTimeField('Срок выполнения')
    start = models.DateTimeField('Начало выполнения')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        # ordering = ('-date',)


class Log(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField('Дата', default=now)
    text = models.TextField('Текст', max_length=50, null=True)

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
        ordering = ('-time',)
