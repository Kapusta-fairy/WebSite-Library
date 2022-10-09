from django.db import models


class ImageLink(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название(для слабовидящих)')
    image = models.ImageField(upload_to='main/%y/%m/%d', verbose_name='Изображение')
    url = models.URLField(max_length=500, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'изображение со ссылкой'
        verbose_name_plural = 'изображения со ссылкой'
