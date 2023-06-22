"""
to render html webpages
"""
 
from django.http import HttpResponse

HTML_STRING = """
<h1>Hello!</h1>
"""

def home_view(request):
    """
    take in request, 
    return html as a response
    """

    return HttpResponse(HTML_STRING)


