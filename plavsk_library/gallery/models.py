from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение галереи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'изображение в галереи'
        verbose_name_plural = 'изображения'
