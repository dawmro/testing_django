from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from recepies.models import RecipeIngredient, Recipe
from .models import Meal, MealStatus

# Create your tests here.

User = get_user_model()




class MealTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('adam', password='pass1234')
        self.user_a_id = self.user_a.id
        self.user_b = User.objects.create_user('badam', password='pass1234')
        self.user_b_id = self.user_b.id
        self.recipe_a = Recipe.objects.create(
            name = 'Grilled Chicken',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name = 'Grilled Chicken Tacos',
            user = self.user_b
        )
        self.recipe_c = Recipe.objects.create(
            name = 'Grilled Pork',
            user = self.user_a
        )
        self.recipe_ingredient_a1 = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name="chicken",
            quantity="1/2",
            unit="pound"
        )
        self.recipe_ingredient_a2 = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name="egg",
            quantity="1",
            unit="oz"
        )
        self.recipe_ingredient_a3 = RecipeIngredient.objects.create(
            recipe=self.recipe_a,
            name="bread",
            quantity="rehdhtt",
            unit="kg"
        )
        self.recipe_ingredient_b1 = RecipeIngredient.objects.create(
            recipe=self.recipe_b,
            name="chicken",
            quantity="1/2",
            unit="pound"
        )
        self.recipe_ingredient_b2 = RecipeIngredient.objects.create(
            recipe=self.recipe_b,
            name="taco",
            quantity="5",
            unit="piece"
        )
        self.meal_a = Meal.objects.create(
            user=self.user_a,
            recipe=self.recipe_a
        )
        self.meal_b = Meal.objects.create(
            user=self.user_a,
            recipe=self.recipe_a,
            status=MealStatus.COMPLETED
        )


    def test_pending_meals(self):
        qs1 = Meal.objects.all().pending()
        self.assertEqual(qs1.count(), 1)
        qs2 = Meal.objects.by_user_id(self.user_a_id).pending()
        self.assertEqual(qs2.count(), 1)

    def test_completed_meals(self):
        qs1 = Meal.objects.all().completed()
        self.assertEqual(qs1.count(), 1)
        qs2 = Meal.objects.by_user_id(self.user_a_id).completed()
        self.assertEqual(qs2.count(), 1)

    def test_add_item_via_toggle(self):
        meal_b = Meal.objects.create(
            user=self.user_a,
            recipe=self.recipe_a,
        )
        qs2 = Meal.objects.by_user_id(self.user_a_id).pending()
        self.assertEqual(qs2.count(), 2)
        added = Meal.objects.toggle_in_queue(user_id=self.user_a_id, recipe_id=self.recipe_c.id)
        qs3 = Meal.objects.by_user_id(self.user_a_id).pending()
        self.assertEqual(qs3.count(), 3)
        self.assertTrue(added)

    def test_remove_item_via_toggle(self):
        added = Meal.objects.toggle_in_queue(user_id=self.user_a_id, recipe_id=self.recipe_a.id)
        qs3 = Meal.objects.by_user_id(self.user_a_id).pending()
        self.assertEqual(qs3.count(), 0)
        self.assertFalse(added)

    