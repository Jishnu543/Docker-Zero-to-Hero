from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        # http://...:8000/
    path('demo/', views.demo, name='demo'),     # http://...:8000/demo
]
