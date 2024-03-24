from django.urls import path
#importing home function from views.py
from .views import home
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name = "base"),
    path('home/', home, name='home'),
    path("delete_item/<int:id>/", views.delete, name = "delete"),
    path("plot", views.plot, name ="plot")
]