from django.http import HttpResponseRedirect
from django.urls import include, path

from ledger import views

urlpatterns = [
    # path('', lambda request: HttpResponseRedirect('/recipes/list/')),
    path("recipes/list/", views.recipe_list, name = "recipe_list"),
    path("recipe/<int:id>/", views.recipe_info, name = "recipe_detail"),
]