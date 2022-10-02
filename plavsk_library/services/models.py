from django.db import models


class Services(models.Model):
    text = models.TextField(verbose_name='Услуга')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'
        ordering = ['text']
