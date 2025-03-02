from django.contrib import admin
from ledger import models
from .models import Ingredient, Recipe, RecipeIngredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity')

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('id','recipe_name')
    search_fields = ['id','recipe_name']
    list_filter = ['id','recipe_name']
    ordering = ['id']

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)