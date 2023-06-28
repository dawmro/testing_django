from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

# create class Articles that inherits from django models.Model
class Article(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models
    # title of an article
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    # content of article
    content = models.TextField()
    # when created
    timestamp = models.DateTimeField(auto_now_add=True)
    # when updated
    updated = models.DateTimeField(auto_now=True)
    # when article has been published
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now)

    # override save method
    def save(self, *args, **kwargs):
        # slugify title if empty
        if self.slug is None:
            self.slug = slugify(self.title)
        # call origina save method
        super().save(*args, **kwargs)

