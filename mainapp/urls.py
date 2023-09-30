"""
URL configuration for mainapp project.

"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from website.sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("", include("website.urls")),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')), # The CKEditor path
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)