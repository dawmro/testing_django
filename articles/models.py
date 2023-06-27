from django.db import models

# Create your models here.

# create class Articles that inherits from django models.Model
class Article(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models
    # title of an article
    title = models.CharField(max_length=100)
    # actual content of article
    content = models.TextField()
