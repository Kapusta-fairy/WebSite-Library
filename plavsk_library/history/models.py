from django.db import models


class History(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    image = models.ImageField(upload_to='history/%y/%m/%d', blank=True, null=True, verbose_name='Изображение')
    caption = models.CharField(max_length=150, blank=True, null=True, verbose_name='Подпись')
    text = models.TextField(blank=True, null=True, verbose_name='Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'историческая информация'
        verbose_name_plural = 'блок информации'

