from django.urls import path
#importing home function from views.py
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),
    path("delete_item/<int:id>/", views.delete, name = "delete"),
    path("plot", views.plot, name ="plot")
]