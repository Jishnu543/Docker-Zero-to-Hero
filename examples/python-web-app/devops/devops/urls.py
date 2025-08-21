from django.urls import path
from . import views   # make sure views.py is imported

urlpatterns = [
    path('', views.index, name='index'),      # existing homepage
    path('demo/', views.index, name='demo'),  # new route for /demo
    path('admin/', admin.site.urls),
]
