from django.db import models


class Staff(models.Model):
    title = models.CharField(max_length=40, verbose_name='Должность')
    department = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Отдел')
    text = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='staff/', blank=True, verbose_name='Изображение')


class Department(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    phone = models.IntegerField(verbose_name='Телефон')
    address = models.CharField(max_length=40, verbose_name='Адрес')
    mode = models.TextField(verbose_name='Режим работы')
