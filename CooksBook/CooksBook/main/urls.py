from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('show_recipes_without_product/<int:product_id>', views.show_recipes_without_product, name='show_recipes_without_product'),
    path('add_product_to_recipe/', views.add_product_to_recipe_view, name='add_product_to_recipe'),
    path('cook_recipe/', views.cook_recipe_view, name='cook_recipe'),
]