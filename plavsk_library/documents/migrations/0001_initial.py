# Generated by Django 3.0 on 2022-09-22 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название документа')),
                ('doc', models.FileField(upload_to='documents/', verbose_name='Документ')),
            ],
        ),
    ]
