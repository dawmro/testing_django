from django.contrib.auth import get_user_model
from django.contrib import admin
from .models import RecipeIngredient, Recipe, RecipeIngredientImage

# Register your models here.

User = get_user_model()  

admin.site.register(RecipeIngredientImage)

class RecipeIngridientInline(admin.StackedInline):
    model = RecipeIngredient
    readonly_fields = ['quantity_as_float', 'as_mks', 'as_imperial']
    #fields = ['name', 'quantity', 'unit', 'directions']
    extra = 0

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngridientInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)