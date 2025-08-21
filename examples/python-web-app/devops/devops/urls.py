from django.contrib import admin
from django.urls import path
from . import views  # import views from devops/devops/views.py

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),  # 👈 add this
    path('admin/', admin.site.urls),
]
