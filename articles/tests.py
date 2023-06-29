from django.test import TestCase

# Create your tests here.

from .models import Article
from django.utils.text import slugify
from .utils import slugify_instance_title

class ArticleTestCase(TestCase):

    def setUp(self):
        print("setUp")
        # create articles for test database
        self.number_of_articles = 500
        for i in range(0, self.number_of_articles):
            Article.objects.create(title='Hello world', content=f"Content of article {i}.")


    # check if there are any article objects in database
    def test_queryset_exists(self):
        print("test_queryset_exists")
        qs = Article.objects.all()
        self.assertTrue(qs.exists())


    # check if there are is correct number article objects in database
    def test_queryset_count(self):
        print("test_queryset_count")
        qs = Article.objects.all()
        self.assertEquals(qs.count(), self.number_of_articles)


    # check if slugification works correctly
    def test_hello_world_slug(self):
        print("test_hello_world_slug")
        # get first article because it's slug hasn't been sufixed with anything
        obj = Article.objects.all().order_by("id").first()
        slug = obj.slug
        title = obj.title
        slugified_title = slugify(title)
        self.assertEqual(slug, slugified_title)


    # check if making slug unique works correctly
    def test_hello_world_slug_unique(self):
        print("test_hello_world_slug_unique")
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


    def test_slugify_instance_title(self):
        print("test_slugify_instance_title")
        obj_first = Article.objects.all().order_by("id").last()
        new_slugs = []
        for i in range(0, 25):
            instance = slugify_instance_title(obj_first, save=False)
            new_slugs.append(instance.slug)

        # remove duplicates from new_slugs
        unique_slugs = list(set(new_slugs))
        # compare lengths to find out if there were any duplicates
        self.assertEqual(len(new_slugs), len(unique_slugs))


    def test_slugify_instance_title_redux(self):
        # get slugs from all objects and put them in list, get single values instead of tuples
        slug_list = Article.objects.all().values_list('slug', flat=True)
        # remove duplicates from new_slugs
        unique_slug_list = list(set(slug_list))
        # compare lengths to find out if there were any duplicates
        self.assertEqual(len(slug_list), len(unique_slug_list))
