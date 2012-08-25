from django.http import HttpResponse
from django.template import Template

def index(request):
    t = django.template.loader.get_template('test.html')
    return t.render()
