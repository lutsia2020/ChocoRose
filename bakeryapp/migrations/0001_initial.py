# Generated by Django 3.2 on 2021-04-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bakery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название выпечки')),
                ('text', models.TextField(max_length=255, verbose_name='Состав выпечки')),
                ('weight', models.IntegerField(max_length=255, verbose_name='Вес выпечки')),
            ],
        ),
    ]
