from django.shortcuts import redirect, render
from.models import Recipe
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
