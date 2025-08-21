from django.contrib import admin
from django.urls import path
from . import views   # make sure views.py exists

urlpatterns = [
    path('', views.index, name='index'),   # homepage only
    path('admin/', admin.site.urls),       # Django admin
]
