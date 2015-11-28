from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello(request):
    t = get_template('base.html')
    html = t.render()
    return HttpResponse(html)

def a(request):
    return HttpResponse("A")

def b(request):
    return HttpResponse("B")

def c(request):
    return HttpResponse("C")
