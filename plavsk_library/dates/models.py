from django.db import models


class Dates(models.Model):
    date = models.CharField(max_length=60, verbose_name='Дата события')
    content = models.TextField(verbose_name='Информация о событии')
    year = models.ForeignKey('years', on_delete=models.PROTECT, verbose_name='Год')

    def __str__(self):
        return self.date

    class Meta:
        verbose_name = 'дата'
        verbose_name_plural = 'даты'
        ordering = ['date']


class Years(models.Model):
    year = models.IntegerField(max_length=4, verbose_name='Год')

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'год'
        verbose_name_plural = 'годы'
        ordering = ['year']
