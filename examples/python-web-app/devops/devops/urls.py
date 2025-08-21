from django.contrib import admin
from django.urls import path
from . import views   # make sure views.py exists

urlpatterns = [
    path('', views.index, name='index'),      # homepage
    path('demo/', views.index, name='demo'),  # /demo route (points to same view)
    path('admin/', admin.site.urls),          # Django admin
]
