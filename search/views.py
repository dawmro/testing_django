from django.shortcuts import render

# Create your views here.
def search_view(request):
    query = request.GET.get("q")

    context = {
        "query": query
    }
    template = "search/results-view.html"

    if request.htmx:
        template = "search/partials/results.html"

    return render(request, template, context=context)