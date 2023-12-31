# Generated by Django 4.2.2 on 2023-08-01 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recepies', '0009_alter_recipeingredient_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('p', 'Pending'), ('c', 'Completed'), ('e', 'Expired'), ('a', 'Aborted')], default='p', max_length=1)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepies.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
