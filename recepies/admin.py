from django.contrib import admin
from .models import RecipeIngridient, Recipe

# Register your models here.

admin.site.register(RecipeIngridient)
admin.site.register(Recipe)