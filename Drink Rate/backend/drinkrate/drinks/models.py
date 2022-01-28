from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.CharField(max_length=255, null=True, verbose_name='Описание')
    rating = models.IntegerField(verbose_name='Рейтинг напитка')
