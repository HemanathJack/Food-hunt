from django import forms
from .models import Recipe, UserProfile
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'profile_image']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EditUsernameForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username']

class EditPasswordForm(PasswordChangeForm):
    pass

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
