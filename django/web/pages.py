from django.http import HttpResponse

def index(request):
    return object_list(request, template_name='test.html')
