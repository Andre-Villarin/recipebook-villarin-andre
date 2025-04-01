from django.shortcuts import get_object_or_404, redirect, render
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe
from django.contrib.auth.decorators import login_required

def list_redirect(request):
    return redirect("recipe_list")

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes}) 

@login_required
def recipe_info(request, id):
     recipe = Recipe.objects.get(id=id)
     return render(request, "recipe_info.html", {"recipe": recipe})

@login_required
def add_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save() 
            return redirect('recipe_info', id=recipe.pk)
    return render(request, "add_recipe.html", {"form": form})

@login_required
def add_image(request, id):
    form = RecipeImageForm(request.POST, request.FILES)
    recipe = get_object_or_404(Recipe, id=id)
    if form.is_valid():
        image = form.save(commit=False)
        image.recipe = Recipe.objects.get(id=id)
        image.save()
        return redirect('recipe_info', id=recipe.id)
    
    return render(request, "add_image.html", {'form': form})