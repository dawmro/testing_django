from django.db import models
from django.conf import settings
from .validators import validate_unit_of_measure
from .utils import number_str_to_float

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


# prepration steps for single ingridient from a given recipe
class RecipeIngridient(models.Model):
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