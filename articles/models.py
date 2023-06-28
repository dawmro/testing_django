from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

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
        #if self.slug is None:
        #    self.slug = slugify(self.title)
        # call origina save method
        super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False):
    slug = slugify(instance.title)
    # filter by slug, exclude current instance
    qs = Article.objects.filter(slug=slug)
    # if slug exists in other instances
    if qs.exists():
        # create new slug using current one
        slug = f"{slug}-{qs.count()+1}"
    instance.slug = slug
    if save:
        instance.save()
    return instance

def article_pre_save(sender, instance, *args, **kwargs):
    print(f"pre_save: {args}, {kwargs}")
    if instance.slug is None:
            slugify_instance_title(instance, save=False)

# connect pre_save signal to article_pre_save receiver function every time Article instance is saved
pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    print(f"post_save: {args}, {kwargs}")
    if created:
        slugify_instance_title(instance, save=True)

# connect post_save signal to article_pre_save receiver function every time after Article instance is saved
post_save.connect(article_post_save, sender=Article)