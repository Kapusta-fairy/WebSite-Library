from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название(для слабовидящих)')
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение галереи')

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'изображения'
