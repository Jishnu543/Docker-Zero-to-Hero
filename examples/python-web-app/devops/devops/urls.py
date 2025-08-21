from django.contrib import admin
from django.urls import path, include   # include is important!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls')),  # <-- include the demo app urls
]
