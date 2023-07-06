from django import forms

from .models import Recipe


class RecipeForm(models.ModelForm):
    class Meta:
        models = Recipe
        fields = ["name", "description", "directions"]