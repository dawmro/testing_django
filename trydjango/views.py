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

    # put data into context dict
    context = {
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    # unpack context dict to html string
    HTML_STRING= """
    <h1>{title} (id: {id})!</h1>
    <p>{content}!</p>
    """.format(**context)


    return HttpResponse(HTML_STRING)


