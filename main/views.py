from django.http import HttpResponse


def index(request):
    return HttpResponse("Test view of Online Store Main")