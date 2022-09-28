# Generated by Django 3.0 on 2022-09-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=60, verbose_name='Дата события')),
                ('content', models.TextField(verbose_name='Информация о событии')),
            ],
            options={
                'verbose_name': 'Даты',
                'verbose_name_plural': 'дата',
                'ordering': ['date'],
            },
        ),
    ]
