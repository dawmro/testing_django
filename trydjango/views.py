"""
to render html webpages
"""
from django.http import HttpResponse
from articles.models import Article
import random


def home_view(request):
    """
    take in request, 
    return html as a response
    """
    random_id = random.randint(1,2)
    article_obj = Article.objects.get(id=random_id)   
    H1_STRING = f"""
    <h1>{article_obj.title} (id: {article_obj.id})!</h1>
    """
    P_STRING = f"""
    <p>{article_obj.content}!</p>
    """
    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)


