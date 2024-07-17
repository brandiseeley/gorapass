from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World. This is Naya and Brandi's super cool app.")