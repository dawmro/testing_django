# Generated by Django 4.2.2 on 2023-07-05 05:30

from django.db import migrations, models
import recepies.validators


class Migration(migrations.Migration):

    dependencies = [
        ('recepies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingridient',
            name='quantity',
            field=models.CharField(max_length=50, validators=[recepies.validators.validate_unit_of_measure]),
        ),
    ]