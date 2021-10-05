from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
]
