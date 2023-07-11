from django.db import models
from django.conf import settings
from .validators import validate_unit_of_measure
from .utils import number_str_to_float
from django.urls import reverse
import pint

# Create your models here.


class Recipe(models.Model):
    # who added recepie
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # name of a dish
    name = models.CharField(max_length=220)
    # short description of a dish
    description = models.TextField(blank=True, null=True)
    # how to make it
    directions = models.TextField(blank=True, null=True)
    # when added
    timestamp = models.DateField(auto_now_add=True)
    # when last updated
    updated = models.DateField(auto_now=True)
    # show or hide recepie
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"id": self.id})

    def get_hx_url(self):
        return reverse("recipes:hx-detail", kwargs={"id": self.id})

    def get_edit_url(self):
        return reverse("recipes:edit", kwargs={"id": self.id})

    def get_ingredients_children(self):
        return self.recipeingredient_set.all()


# prepration steps for single ingridient from a given recipe
class RecipeIngredient(models.Model):
    # attach to parent class
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220) 
    description = models.TextField(blank=True, null=True)
    # users can put in different things, make it char just to be safe
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    # pounds, lbs, oz, gram
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    directions = models.TextField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.recipe.id,
            "id": self.id
        }
        return reverse("recipes:hx-ingredient-detail", kwargs=kwargs)

    def convert_to_system(self, system="mks"):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement #.to_base_units()

    def as_mks(self):
        # meter, gram, second
        measurement = self.convert_to_system(system='mks')
        return measurement.to_base_units()

    def as_imperial(self):
        # mile, puond, second
        measurement = self.convert_to_system(system='imperial')
        return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)

'''
class RecipeImage(models.Model):
    # attach to parent class
    recipe = models.ForeignKey(Recipe)
'''