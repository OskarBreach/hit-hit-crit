from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import get_object_or_404

def home(request):
    template = loader.get_template('homepage.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
