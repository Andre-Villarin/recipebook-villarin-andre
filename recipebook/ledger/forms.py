from django import forms

from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']