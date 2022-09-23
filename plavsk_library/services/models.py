from django.db import models


class Services(models.Model):
    text = models.TextField(verbose_name='Услуга')
