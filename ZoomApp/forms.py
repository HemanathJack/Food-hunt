from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
    
    ingredients = forms.JSONField(widget=forms.HiddenInput(), required=False)
    steps = forms.JSONField(widget=forms.HiddenInput(), required=False)

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['ingredients']

    ingredients = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))

IngredientFormSet = forms.formset_factory(IngredientForm, extra=1)

class StepForm(forms.Form):
    class Meta:
        model = Recipe
        fields = ['steps']

    steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-textarea'}))

StepFormSet = forms.formset_factory(StepForm, extra=1)
