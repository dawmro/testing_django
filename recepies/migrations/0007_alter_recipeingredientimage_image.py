# Generated by Django 4.2.2 on 2023-07-15 03:05

from django.db import migrations, models
import recepies.models


class Migration(migrations.Migration):

    dependencies = [
        ('recepies', '0006_alter_recipeingredientimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to=recepies.models.recipe_ingredient_image_upload_handler),
        ),
    ]