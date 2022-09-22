from django.db import models


class HistoryImageNoCaption(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')


class HistoryImageCaption(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
    caption = models.CharField(max_length=50, verbose_name='Подпись')


class HistoryTextInfo(models.Model):
    text = models.TextField(verbose_name='Текст')
