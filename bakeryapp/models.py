from django.db import models
# Create your models here.

# категории выпечки
class BakeryCategory(models.Model):
    name = models.CharField(verbose_name="Категория выпечки", max_length=255)

    # отображение названия объекта
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория выпечки'
        verbose_name_plural = 'Категория выпечки'


# описание выпечки
class Bakery(models.Model):
    category=models.ForeignKey(BakeryCategory, on_delete=models.CASCADE, default=1, verbose_name="Kатегория выпечки")
    name=models.CharField(max_length=255, verbose_name="Название выпечки")
    text=models.TextField(max_length=255, verbose_name="Состав выпечки")
    weight=models.IntegerField(verbose_name="Вес выпечки")
    image=models.ImageField(verbose_name="Картинка выпечки", blank=True)
    price = models.IntegerField(verbose_name="Цена выпечки")

    # отображение названия объекта
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Конкретная выпечка'
        verbose_name_plural = 'Конкретные выпечки'

# выбор вида выпечки

class BakeryBasis(models.Model):
    name = models.CharField(verbose_name="Основа выпечки", max_length=255)

    # отображение названия объекта
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Основа выпечки'
        verbose_name_plural = 'Основа выпечки'

class BakeryCream(models.Model):
    name = models.CharField(verbose_name="Крем выпечки", max_length=255)
    price = models.IntegerField(verbose_name="Цена за крем выпечки", default=0)

    # отображение названия объекта
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Крем выпечки'
        verbose_name_plural = 'Кремы выпечки'

class BakeryFilling(models.Model):
    name = models.CharField(verbose_name="Начинка выпечки", max_length=255)
    price = models.IntegerField(verbose_name="Цена за начинку выпечки", default=0)

    # отображение названия объекта
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Начинка выпечки'
        verbose_name_plural = 'Начинки выпечки'

# консруктор по созданию выпечки

class BakeryСonsist(models.Model):
    customer=models.CharField(verbose_name="Имя заказчика", max_length=255)
    phone=models.CharField(verbose_name="Телефон заказчика", max_length=255)
    name = models.ForeignKey(Bakery, on_delete=models.CASCADE, default=1, verbose_name="Выберите выпечку")
    basis=models.ForeignKey(BakeryBasis, on_delete=models.CASCADE, default=1, verbose_name="Основа выпечки")
    cream=models.ForeignKey(BakeryCream, on_delete=models.CASCADE, default=1, verbose_name="Крем выпечки")
    filling=models.ForeignKey(BakeryFilling, on_delete=models.CASCADE,default=1, verbose_name="Начинка выпечки")
    price=models.IntegerField(verbose_name="Общая цена выпечки")
    # отображение названия объекта
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Детали заказа выпечек'
