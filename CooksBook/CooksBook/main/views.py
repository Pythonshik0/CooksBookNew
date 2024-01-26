from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe_view(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        product_id = request.POST.get('product_id')
        weight = request.POST.get('weight')

        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            product = Product.objects.get(pk=product_id)
        except (Recipe.DoesNotExist, Product.DoesNotExist):
            return JsonResponse({'error': 'Recipe or Product not found'}, status=404)

        recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product, defaults={'weight': weight})

        if not created:
            recipe_product.weight = weight
            recipe_product.save()

        return JsonResponse({'message': 'Product added to recipe successfully'})

    return render(request, 'add_product_to_recipe.html')


def cook_recipe_view(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        if recipe_id:
            try:
                recipes = RecipeProduct.objects.filter(recipe_id=recipe_id)
                for recipe in recipes:
                    recipe.product.times_used += 1
                    recipe.product.save()

                return JsonResponse({'message': 'Recipes cooked successfully'})
            except Recipe.DoesNotExist:
                return JsonResponse({'error': 'Recipe not found'}, status=404)
        else:
            return render(request, 'cook_recipe.html')


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product,
                                                     recipeproduct__weight__gte=10).distinct()
    return render(request, 'recipe_without_product.html', {'product': product, 'recipes': recipes_without_product})