# config/urls.py
from django.contrib import admin
from django.urls import path, include

from tree.views import load_home
from account.views import (
    home_screen_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login'),
]
