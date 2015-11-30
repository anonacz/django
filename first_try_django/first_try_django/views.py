from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello(request, name=1):
    headers = '<br />\n'.join(['%s -- %s' % (k, v) for k, v in request.META.iteritems()])
    t = get_template('base.html')
    html = t.render()
    c = Context({'name': name, 'headers': headers})
    return HttpResponse(t.render(c))

def a(request):
    return HttpResponse("A")

def b(request):
    return HttpResponse("B")

def c(request):
    return HttpResponse("C")
