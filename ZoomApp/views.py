from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

# Models 
from .models import *

# Forms
from .forms import RecipeForm, IngredientFormSet, StepFormSet

def login(request):
    return render(request, 'login.html')

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes':recipes})


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        return render(request, 'home.html', {'recipes': recipes})
    
def recipe_list(request):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        ingredients_list = (recipe.ingredients).split()
        first_three_ingredients = ' '.join(ingredients_list[:3])
        print(first_three_ingredients)
    return render(request, 'recipe_list.html', {'recipes':recipes,'first_three_ingredients':first_three_ingredients})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    # ingredients_list = recipe.ingredients.split(',')
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def create_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        steps = request.POST.get('steps')
        meal_type = request.POST.get('meal_type')
        cooking_time = request.POST.get('cooking_time')
        cuisines = request.POST.get('cuisines')
        image = request.FILES.get('image')

        author = request.user
        
        # print("Title:", title)
        # print("Description:", description)
        # print("Ingredients:", ingredients)
        # print("Steps:", steps)
        # print("Meal Type:", meal_type)
        # print("Cooking Time:", cooking_time)
        # print("Cuisines:", cuisines)
        # print("Image:", image)
        
        recipe = Recipe(
            title=title,
            description=description,
            ingredients=ingredients,
            steps=steps,
            meal_type=meal_type,
            cooking_time=cooking_time,
            cuisines=cuisines,
            author=author,
            image=image
        )
        recipe.save()
        # print(recipe)
        
        return redirect('recipe_list')  # Redirect to a recipe list page
    
    return render(request, 'recipe_detail.html', {})


def update_recipe(request, recipe_pk):
    recipe = get_object_or_404(Recipe, pk = recipe_pk)
    if recipe.author != request.user:
        return render(request, 'recipe_detail.html')
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'update_recipe.html', {'form':form})

def delete_recipe(request, pk):
    print(Recipe, pk=pk)
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')