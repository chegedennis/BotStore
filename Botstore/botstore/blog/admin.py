from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "last_updated", "published_date")
    list_filter = ("status", "last_updated", "published_date")
    search_fields = ("title", "content")
    actions = ["make_published"]

    @admin.action(description="Mark selected posts as Published")
    def make_published(self, request, queryset):
        queryset.update(status="published")
