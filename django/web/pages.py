from django.http import HttpResponse

def index(request):
    page = """ <h1>Hello, World!</h1><img src="{{ STATIC_URL }}vetlogo.jpg" /> """
    return HttpResponse(page)
