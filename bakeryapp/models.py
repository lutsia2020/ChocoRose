from django.db import models
# Create your models here.

class Bakery(models.Model):
    name=models.CharField(max_length=255, verbose_name="Название выпечки")
    text=models.TextField(max_length=255, verbose_name="Состав выпечки")
    weight=models.IntegerField(verbose_name="Вес выпечки")
    image=models.ImageField(verbose_name="Картинка выпечки", blank=True)

class BakeryCategory(models.Model):
        name = models.CharField(verbose_name="Категория выпечки", max_length=200)

    def __str__(self):
        return self.name


