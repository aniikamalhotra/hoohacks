from django.urls import path
#importing home function from views.py
from .views import home


urlpatterns = [
    path('', home, name='home'),
]