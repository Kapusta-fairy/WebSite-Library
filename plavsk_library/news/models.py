from django.db import models


class News(models.Model):
    title = models.CharField(max_length=40, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')
    video = models.FileField(upload_to='news/video/%y/%m/%d', blank=True, verbose_name='Видео')
    utube = models.URLField(blank=True, verbose_name='Ссылка на YouTube видео')
    image1 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 1')
    image2 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 2')
    image3 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 3')
    image4 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 4')
    image5 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 5')
    image6 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 6')
    image7 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 7')
    image8 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 8')
    image9 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 9')
    image10 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 10')
    image11 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 11')
    image12 = models.ImageField(upload_to='news/image/%y/%m/%d', blank=True, null=True, verbose_name='Изображение 12')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['title']
