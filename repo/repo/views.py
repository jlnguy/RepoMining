from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response("repo/home_page.html")

def error(request):
    response = render_to_response('404.html', {},
                                  context_instance = RequestContext(request))
    response.status_code = 404
    return response
