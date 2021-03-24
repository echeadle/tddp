
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('lists.urls')),
    path('my-backend/', admin.site.urls),
]
