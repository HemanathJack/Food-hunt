from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    MEAL_TYPES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
        ('Dessert', 'Dessert'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.TextField()
    image = models.ImageField(upload_to="recipe_image/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    cooking_time = models.PositiveIntegerField()  # In minutes
    cuisines = models.ManyToManyField(Cuisine)

    def __str__(self):
        return self.title
