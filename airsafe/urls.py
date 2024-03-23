from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # including the codebase urls.py file
    path('', include('airsafeapp.urls'))
]