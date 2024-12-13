from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "last_updated")
    list_filter = ("published_date", "last_updated")
    search_fields = ("title", "content")
