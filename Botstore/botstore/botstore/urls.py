from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from products.views import home

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("admin/", admin.site.urls),  # Admin panel
    path("product/", include("products.urls")),  # Products app URLs (prefix "product/")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
