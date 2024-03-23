from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello traveler! Welcome to AirSafe baddies!")