from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include  # Include is required

from products.views import home  # Home view

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("admin/", admin.site.urls),  # Admin panel
    path("product/", include("products.urls")),  # Products app URLs
    path("blog/", include("blog.urls")),  # Blog app URLs
]

if settings.DEBUG:  # Serve media files in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
