from django.db import models


class Documents(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название документа')
    doc = models.FileField(upload_to='documents/', verbose_name='Документ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'
        ordering = ['name']
