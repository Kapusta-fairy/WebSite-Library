from django.db import models


class Department(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    address = models.CharField(max_length=40, verbose_name='Адрес')
    schedule = models.TextField(verbose_name='Режим работы')
