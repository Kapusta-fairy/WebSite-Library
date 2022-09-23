from django.db import models


class News(models.Model):
    title = models.CharField(max_length=40, blank=True, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')
    image = models.ImageField(upload_to='news/image/', blank=True, verbose_name='Изображение')
    video = models.FileField(upload_to='news/video/', blank=True, verbose_name='Видео')
    utube = models.URLField(blank=True, verbose_name='Ссылка на видео на YouTube')
