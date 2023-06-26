from django.shortcuts import render

from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
# Create your views here.

def article_search_view(request):
    query_dict = request.GET
    
    # check if query is int
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        "object": article_obj,
    }

    return render(request, "articles/search.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id) 

    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)


@login_required
def article_create_view(request):
    # create form to be rendered
    form = ArticleForm()
    context = {
        "form": form,
    }

    if request.method == "POST":
        # pass all data to instance of class
        form = ArticleForm(request.POST)
        # validate data
        if form.is_valid():
            # get cleaned data from form
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            article_object = Article.objects.create(title=title, content=content)
            context["object"] = article_object
            context["created"] = True

    return render(request, "articles/create.html", context=context)