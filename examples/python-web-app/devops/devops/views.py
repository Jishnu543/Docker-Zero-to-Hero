from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")

def demo(request):
    return HttpResponse("<h1>This is the Demo Page!</h1>")
