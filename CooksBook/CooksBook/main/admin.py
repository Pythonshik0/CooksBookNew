from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct  # Используем нашу промежуточную модель вместо through-модели
    extra = 1
    fields = ['product', 'weight']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]