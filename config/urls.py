# config/urls.py
from django.contrib import admin
from django.urls import path, include

from tree.views import load_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', load_home, name='home'),
]
