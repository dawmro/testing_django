from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import RecipeIngredient, Recipe

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
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 3)

    def test_user_two_level_relationship(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 5)

    def test_user_two_level_reverse_relationship(self):
        user = self.user_a
        recipe_ingredient_ids = list(user.recipe_set.all().values_list("recipeingredient__id", flat=True))
        # [1, 2, 3, None]
        qs = RecipeIngredient.objects.filter(id__in=recipe_ingredient_ids)
        self.assertEqual(qs.count(), 5)

    def test_user_two_level_reverse_relationship_via_recipe(self):
        user = self.user_a
        ids = user.recipe_set.all().values_list("id", flat=True)
        qs = RecipeIngredient.objects.filter(recipe_id__in=ids)
        self.assertEqual(qs.count(), 5)

    def test_unit_measure_validation_pass(self):
        valid_unit = 'ounce'
        ingridient = RecipeIngredient(
            name="new",
            quantity=10,
            recipe=self.recipe_a,
            unit=valid_unit
        )
        # verify if all fields are valid
        ingridient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_unit = ['yellow', 'chungus', 'bread', 'arefsfsdfg']
        for inv_unit in invalid_unit:
            with self.assertRaises(ValidationError):
                ingridient = RecipeIngredient(
                    name="new",
                    quantity=10,
                    recipe=self.recipe_a,
                    unit=inv_unit
                )
                # verify if all fields are valid
                ingridient.full_clean()

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a2.quantity_as_float)
        self.assertIsNone(self.recipe_ingredient_a3.quantity_as_float)