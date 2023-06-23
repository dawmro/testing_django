"""
to render html webpages
"""
from django.http import HttpResponse
from articles.models import Article
import random
from django.template.loader import render_to_string

def home_view(request):
    """
    take in request, 
    return html as a response
    """
    random_id = random.randint(1,2)
    article_obj = Article.objects.get(id=random_id)   
    articles_queryset = Article.objects.all() 
    
    # put data into context dict
    context = {
        "articles_list": articles_queryset,
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content,
    }
    HTML_STRING = render_to_string("home-view.html", context=context) 

    return HttpResponse(HTML_STRING)


