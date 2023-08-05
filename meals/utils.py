from django.contrib.auth import get_user_model
from django.db.models import Sum

from meals.models import Meal
from recepies.models import RecipeIngredient

User = get_user_model()
j = User.objects.first()

def generate_meal_queue_total(user):
    queue = Meal.objects.get_queue(user=user, prefetch_ingredients=True)
    ids = queue.values_list("recipe__recipeingredient__id", flat=True)
    qs = RecipeIngredient.objects.filter(id__in=ids)
    return qs.values("name", "unit").annotate(total=Sum("quantity_as_float"))
