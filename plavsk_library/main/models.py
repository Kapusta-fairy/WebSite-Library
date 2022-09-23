from django.db import models


class ImageLink(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
    url = models.URLField(max_length=500, verbose_name='Ссылка')
