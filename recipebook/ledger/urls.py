from django.http import HttpResponseRedirect
from django.urls import include, path

from ledger import views

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/recipes/list/')),
    path("recipes/list/", views.recipe_list, name = "recipe_list"),
    path("recipe/1/", views.recipe_1, name = "recipe_1"),
    path("recipe/2/", views.recipe_2, name = "recipe_2"),
]