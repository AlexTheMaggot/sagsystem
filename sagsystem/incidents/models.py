from django.db import models
from mainapp.models import Workers, Functions, Departments
from django.contrib.auth.models import User


class Incidents(models.Model):
    date = models.DateTimeField(verbose_name='Дата и время')
    worker = models.ForeignKey(Workers, on_delete=models.PROTECT, verbose_name='Сотрудник')
    department = models.ForeignKey(Departments, on_delete=models.PROTECT, verbose_name='Отдел')
    comment = models.TextField(verbose_name='Комментарий')
    adder = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Кем добавлен')
    file = models.FileField(verbose_name='Файл', upload_to='static/incidents/')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'
