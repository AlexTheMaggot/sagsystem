from django.db import models


class Functions(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    function_slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Departments(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    department_slug = models.SlugField(verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Workers(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=200)
    last_name = models.CharField(verbose_name='Фамилия', max_length=200)
    department = models.ForeignKey(Departments, verbose_name='Отдел', on_delete=models.PROTECT)
    function = models.ForeignKey(Functions, verbose_name='Должность', on_delete=models.PROTECT)
    worker_slug = models.SlugField(unique=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Measure(models.Model):
    name = models.CharField(max_length=200)
