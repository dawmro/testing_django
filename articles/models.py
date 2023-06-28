from django.db import models
from django.utils import timezone

# Create your models here.

# create class Articles that inherits from django models.Model
class Article(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models
    # title of an article
    title = models.CharField(max_length=100)
    # content of article
    content = models.TextField()
    # when created
    timestamp = models.DateTimeField(auto_now_add=True)
    # when updated
    updated = models.DateTimeField(auto_now=True)
    # when article has been published
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now)

