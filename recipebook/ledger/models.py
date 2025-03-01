from django.db import models, reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        self.name

    class Meta:
        unique_together = ['name']

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)

    def __str__(self):
        self.recipe_name

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
        self.name