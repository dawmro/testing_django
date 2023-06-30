from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import Http404
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

# Create your views here.

def article_search_view(request):
    query = request.GET.get('q')

    qs = Article.objects.all()
    if query is not None:
        lookups = Q(title__icontains=query) | Q(content__icontains=query)
        qs = Article.objects.filter(lookups)

    context = {
        "object_list": qs,
    }

    return render(request, "articles/search.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    try:
        article_obj = Article.objects.get(slug=slug) 
    except Article.DoesNotExist:
        raise Http404
    except Article.MultipleObjectsReturned:
        article_obj = Article.objects.filter(slug=slug).first() 
    except:
        raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)


@login_required
def article_create_view(request):
    # take data from POST request or create form to be rendered
    form = ArticleForm(request.POST or None)
    context = {
        "form": form,
    }
    # validate data
    if form.is_valid():
        # get cleaned/validated data from form and save it
        article_object = form.save()
        # initialize new empty form, to clear form after submit
        form = ArticleForm()
        context["object"] = article_object
        context["created"] = True
        return redirect(article_object.get_absolute_url())

    return render(request, "articles/create.html", context=context)