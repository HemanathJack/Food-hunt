from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'meal_type', 'cooking_time', 'cuisines', 'ingredients', 'steps', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control custom-input'}),
            'meal_type': forms.Select(attrs={'class': 'form-control custom-input'}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control custom-input'}),
            'cuisines': forms.SelectMultiple(attrs={'class': 'form-control custom-input'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control custom-input'}),
            'steps': forms.Textarea(attrs={'class': 'form-control custom-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control custom-input'}),
        }
