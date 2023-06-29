from django.test import TestCase

# Create your tests here.

from .models import Article

class ArticleTestCase(TestCase):

    def setUp(self):
        # create article for test database
        Article.objects.create(title='Hello world', content='Content of article.')

    # check if there are any article objects in database
    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())