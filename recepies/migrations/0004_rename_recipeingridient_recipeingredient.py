# Generated by Django 4.2.2 on 2023-07-06 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recepies', '0003_recipeingridient_quantity_as_float_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeIngridient',
            new_name='RecipeIngredient',
        ),
    ]
