from django.contrib import admin
from ledger import models
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInLine, ]

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

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    list_display = ('id','description')

admin.site.unregister(models.User)
admin.site.register(models.User, UserAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)