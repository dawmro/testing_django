from django.test import TestCase

# Create your tests here.

from .models import Article
from django.utils.text import slugify


class ArticleTestCase(TestCase):

    def setUp(self):
        # create articles for test database
        self.number_of_articles = 5
        for i in range(0, self.number_of_articles):
            Article.objects.create(title='Hello world', content=f"Content of article {i}.")


    # check if there are any article objects in database
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())


    # check if there are is correct number article objects in database
    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEquals(qs.count(), self.number_of_articles)


    # check if slugification works correctly
    def test_hello_world_slug(self):
        # get first article because it's slug hasn't been sufixed with anything
        obj = Article.objects.all().order_by("id").first()
        slug = obj.slug
        title = obj.title
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)


    # check if making slug unique works correctly
    def test_hello_world_slug_unique(self):
        # get first article because it's slug hasn't been sufixed with anything
        obj_first = Article.objects.all().order_by("id").first()
        title = obj_first.title
        slugified_title = slugify(title)
        # get all articles except of first article because it's slug hasn't been sufixed with anything
        qs = Article.objects.exclude(slug__iexact=slugified_title)
        for obj in qs:
            slug = obj.slug
            title = obj.title
            slugified_title = slugify(title)
            self.assertNotEqual(slug, slugified_title)