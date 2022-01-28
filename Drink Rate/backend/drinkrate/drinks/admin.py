from django.contrib import admin

from .models import Drink


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'rating']
