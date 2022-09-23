from django.db import models


class Dates(models.Model):
    date = models.CharField(max_length=60, verbose_name='Дата события')
    content = models.TextField(verbose_name='Информация о событии')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'Даты'
        verbose_name_plural = 'дата'
        ordering = ['date']
