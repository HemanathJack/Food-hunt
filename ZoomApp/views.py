from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

# Models 
from .models import *

# Forms
from .forms import RecipeForm

def login(request):
    return render(request, 'login.html')

def home(request):
    recipes = Recipe.objects.all()
    cuisines = Cuisine.objects.all()
    ingredients =Ingredient.objects.all()
    form = RecipeForm()
    return render(request, 'home.html', {'recipes':recipes, 'form':form, 'cuisines': cuisines, 'ingredients':ingredients})

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        return render(request, 'home.html', {'recipes': recipes})
    
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes':recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    # ingredients_list = recipe.ingredients.split(',')
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def create_recipe(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        steps = request.POST['steps']
        uploaded_image = request.FILES['image']
        meal_type = request.POST['meal_type']
        cooking_time = request.POST['cooking_time']
        cuisines_ids = request.POST.getlist('cuisines')  # List of cuisine IDs
        ingredients_ids = request.POST.getlist('ingredients')  # List of ingredient IDs

        recipe = Recipe.objects.create(
            title=title,
            description=description,
            steps=steps,
            image=uploaded_image,
            meal_type=meal_type,
            cooking_time=cooking_time,
            author=request.user
        )

        # Assign cuisines using the .set() method with IDs
        recipe.cuisines.set(cuisines_ids)

        # Assign ingredients using the .set() method with IDs
        recipe.ingredients.set(ingredients_ids)

        return redirect('recipe_list')

    return render(request, 'home.html', {})


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