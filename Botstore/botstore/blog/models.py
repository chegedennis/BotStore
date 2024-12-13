from django.db import models
from django_ckeditor_5.fields import CKEditor5Field  # Correct field import


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200)
    content = CKEditor5Field(config_name="extends", blank=True)  # Using CKEditor 5
    cover_image = models.ImageField(upload_to="blog_covers/", blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )  # Status field

    def __str__(self):
        return self.title
