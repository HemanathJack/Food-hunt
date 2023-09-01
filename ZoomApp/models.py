from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=False)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)

    def __str__(self):
        return self.user.username
    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()


class Recipe(models.Model):
    MEAL_TYPES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
        ('Dessert', 'Dessert'),
    ]

    CUISINE_CHOICES = [
        ('Italian', 'Italian'),
        ('Indian', 'Indian'),
        ('Chinese', 'Chinese'),
        ('Mexican', 'Mexican'),
        # Add more cuisine choices here
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.JSONField(blank=True, null=True)
    steps = models.JSONField(blank=True, null=True)
    image = models.ImageField(upload_to="recipe_image/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES, default='Breakfast')
    cooking_time = models.PositiveIntegerField(default=0)  # In minutes
    cuisines = models.CharField(max_length=20, choices=CUISINE_CHOICES, default="Indian")

    def save(self, *args, **kwargs):
        if self.ingredients is None:
            self.ingredients = []  # Set a default value as an empty list
        if self.steps is None:
            self.steps = []  # Set a default value as an empty list
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
