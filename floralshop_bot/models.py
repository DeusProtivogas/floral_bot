from django.db import models

# Create your models here.

class Bouquet(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Модель букета",
    )
    ru_name = models.CharField(
        max_length=100,
        verbose_name="Название букета",
    )
    occasion = models.CharField(
        max_length=100,
        verbose_name="Причина",
    )
    description = models.CharField(
        max_length=200,
        verbose_name="Описание",
    )
    composition = models.CharField(
        max_length=200,
        verbose_name="Состав",
    )
    price = models.IntegerField(
        verbose_name="Цена",
    )

    def __str__(self):
        return f"{self.ru_name} - {self.occasion} - {self.price}"

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'


class Order(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя и фамилия клиента",
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Адрес",
    )
    date = models.CharField(
        max_length=200,
        verbose_name="Дата доставки",
    )
    time = models.CharField(
        max_length=200,
        verbose_name="Время доставки",
    )
    bouquet = models.ForeignKey(
        Bouquet,
        verbose_name="Букет",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name} - {self.date} - {self.time} - {self.bouquet.name}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
