from django.db import models


class ImageLink(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название(для слабовидящих)')
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
    url = models.URLField(max_length=500, verbose_name='Ссылка')

    def __str__(self):
        return str(f'Картинка №{self.pk}')

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документ'
