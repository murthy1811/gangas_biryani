from django.contrib import admin
from .models import Dish, Category

# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Dish, DishAdmin)
admin.site.register(Category, CategoryAdmin)

