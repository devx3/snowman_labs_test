from django.http import HttpResponse


def index(request): 
    return HttpResponse("<h1>Welcome to Tourist Spot's API.</h1>")