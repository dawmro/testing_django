from django.db import models

# Create your models here.

# create class Articles that inherits from django models.Model
class Article(models.Model):
    # title of an article
    title = models.TextField()
    # actual content of article
    content = models.TextField()
