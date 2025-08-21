from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to the Index Page</h1>")

def demo(request):
    return HttpResponse("<h1>Hello from the /demo endpoint!</h1>")
