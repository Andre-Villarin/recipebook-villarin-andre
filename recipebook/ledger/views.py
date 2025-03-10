from django.shortcuts import redirect, render
from.models import Recipe

def list_redirect(request):
    return redirect("recipe_list")

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes}) 

def recipe_info(request, id):
     recipe = Recipe.objects.get(id=id)
     return render(request, "recipe_info.html", {"recipe": recipe})
