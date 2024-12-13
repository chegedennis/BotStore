from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # Include is required

from products.views import home  # Home view

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("admin/", admin.site.urls),  # Admin panel
    path("products/", include("products.urls")),  # Products app URLs
    path("blog/", include("blog.urls")),  # Blog app URLs
    path("ckeditor5/", include("django_ckeditor_5.urls")),  # CKEditor 5 URLs
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
