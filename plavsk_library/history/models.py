from django.db import models


class History(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название(для слабовидящих)')
    image = models.ImageField(upload_to='history/', blank=True, null=True, verbose_name='Изображение')
    caption = models.CharField(max_length=150, blank=True, null=True, verbose_name='Подпись')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')

    class Meta:
        verbose_name = 'Историческая информация'
        verbose_name_plural = 'блок информации'
