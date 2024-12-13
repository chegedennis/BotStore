from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    cover_image = models.ImageField(
        upload_to="blog_covers/", blank=True, null=True
    )  # Cover image field
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)  # Last updated field

    def __str__(self):
        return self.title
