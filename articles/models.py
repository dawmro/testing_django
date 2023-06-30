from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import slugify_instance_title

# Create your models here.

class ArticleQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none() # empty list []
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookups)

class ArticleManager(models.Manager):
    # override get_queryset method
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def search(self, query=None): 
        return self.get_queryset().search(query=query)

# create class Article that inherits from django models.Model
class Article(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models
    # title of an article
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    # content of article
    content = models.TextField()
    # when created
    timestamp = models.DateTimeField(auto_now_add=True)
    # when updated
    updated = models.DateTimeField(auto_now=True)
    # when article has been published
    publish = models.DateField(auto_now_add=False, auto_now=False, default=timezone.now)

    objects = ArticleManager()

    #
    def get_absolute_url(self):
        #return f"/articles/{self.slug}"
        return reverse("article-detail", kwargs={"slug": self.slug})

    # override save method
    def save(self, *args, **kwargs):
        # slugify title if empty
        #if self.slug is None:
        #    self.slug = slugify(self.title)
        # call origina save method
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    # print(f"pre_save")
    if instance.slug is None:
            slugify_instance_title(instance, save=False)

# connect pre_save signal to article_pre_save receiver function every time Article instance is saved
pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    # print(f"post_save")
    # if slug has never been generated, create it
    if created:
        slugify_instance_title(instance, save=True)

# connect post_save signal to article_pre_save receiver function every time after Article instance is saved
post_save.connect(article_post_save, sender=Article)