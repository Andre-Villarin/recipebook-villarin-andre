from django.urls import include, path

from ledger import views

urlpatterns = [
    path("", views.list_redirect, name = "list_redirect"),
    path("recipes/list/", views.recipe_list, name = "recipe_list"),
    path("recipe/<int:id>/", views.recipe_info, name = "recipe_info"),
    path("recipe/add/", views.add_recipe, name = "add_recipe"),
    ]