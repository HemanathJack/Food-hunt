from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import authenticate, login, logout

# Models 
from .models import *

# Forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import RecipeForm, UserProfileForm, LoginForm, EditUsernameForm, EditPasswordForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Automatically log in the newly registered user
            return redirect('home')  # Redirect to the user's profile
    else:
        return render(request, 'registration/register.html', {"register":"register"})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the user's profile
        else:
            return render(request, 'registration/register.html', {"login_form":"login_form", 'login_error':True})
    return render(request, 'registration/register.html', {'login_form': 'login_form'})

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        username_form = EditUsernameForm(request.POST, instance=request.user)
        password_form = EditPasswordForm(request.user, request.POST)
        if form.is_valid() and username_form.is_valid() and password_form.is_valid():
            form.save()
            # username_form.save()
            # password_form.save()
            return redirect('home')  # Redirect to the user's profile
    else:
        form = UserProfileForm(instance=user_profile)
        username_form = EditUsernameForm(instance=request.user)
        password_form = EditPasswordForm(request.user)
    return render(request, 'registration/register.html', {'edit_form': form,
        'username_form': username_form,
        'password_form': password_form,})

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home.html', {'recipes':recipes})

# class CustomLogoutView(LogoutView):
#     def dispatch(self, request, *args, **kwargs):
#         recipes = Recipe.objects.all()
#         return render(request, 'home.html', {'recipes': recipes})
    
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes':recipes})

def recipe_detail(request, recipe_id):
    user = request.user
    recipe = get_object_or_404(Recipe, id=recipe_id)
    # ingredients_list = recipe.ingredients.split(',')
    return render(request, 'recipe_detail.html', {'recipe': recipe,'user': user})

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
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')