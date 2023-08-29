from typing import Optional
from django.contrib import admin
from django.contrib.auth.models import Permission
from django.http.request import HttpRequest
from .models import Ingredient, Cuisine, Recipe

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Recipe)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'admin__username')

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.author == request.user:
            return True
        return super().has_change_permission(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.author == request.user:
            return True
        return super().has_delete_permission(request, obj)