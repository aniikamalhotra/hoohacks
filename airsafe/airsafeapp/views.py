from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello! Welcome to the AirSafe App!")