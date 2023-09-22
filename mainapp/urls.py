"""
URL configuration for mainapp project.

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("website.urls")),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
