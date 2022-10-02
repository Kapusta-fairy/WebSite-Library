from django.db import models


class Staff(models.Model):
    title = models.CharField(max_length=40, verbose_name='Должность')
    department = models.ForeignKey('info.department', on_delete=models.PROTECT, verbose_name='Отдел')
    text = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='staff/', blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
        ordering = ['title']
