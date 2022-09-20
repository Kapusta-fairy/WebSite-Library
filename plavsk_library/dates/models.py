from django.db import models


class Dates(models.Model):
    date = models.CharField(max_length=40, verbose_name='Дата события')
    content = models.TextField(verbose_name='Информация о событии')
