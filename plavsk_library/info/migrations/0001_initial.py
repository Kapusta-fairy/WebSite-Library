# Generated by Django 3.0 on 2022-09-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('address', models.CharField(max_length=40, verbose_name='Адрес')),
                ('schedule', models.TextField(verbose_name='Режим работы')),
            ],
        ),
    ]
