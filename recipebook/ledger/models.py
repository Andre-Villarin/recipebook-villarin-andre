from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    short_bio = models.TextField(max_length=255, blank=True)

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['name']

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.recipe_name

    def get_absolute_url(self):
        return reverse('recipe_info', args=[str(self.id)])
    
    class Meta:
        unique_together = ['recipe_name']

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name="ingredients")
    
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name="recipes")
    
    quantity = models.CharField(max_length=255)

    def __str__(self):
        return self.quantity
    
class RecipeImage(models.Model):
    
    image = models.ImageField(upload_to="recipe_images/", null=False)
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name="images")
    
    def __str__(self):
        return self.description
    