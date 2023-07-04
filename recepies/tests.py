from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import RecipeIngridient, Recipe
# Create your tests here.

User = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):
        self.user_a = User.objects.create_user('adam', password='pass1234')

    def test_user_pw(self):
        checked = self.user_a.check_password('pass1234')
        self.assertTrue(checked)


class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('adam', password='pass1234')
        self.recipe_a = Recipe.objects.create(
            name = 'Grilled Chicken',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name = 'Grilled Chicken Tacos',
            user = self.user_a
        )
        self.recipe_ingredient_a1 = RecipeIngridient.objects.create(
            recipe=self.recipe_a,
            name="chicken",
            quantity="1/2",
            unit="pound"
        )
        self.recipe_ingredient_a2 = RecipeIngridient.objects.create(
            recipe=self.recipe_a,
            name="egg",
            quantity="1",
            unit="oz"
        )
        self.recipe_ingredient_a3 = RecipeIngridient.objects.create(
            recipe=self.recipe_a,
            name="bread",
            quantity="1/2",
            unit="kg"
        )


    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = RecipeIngridient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 3)