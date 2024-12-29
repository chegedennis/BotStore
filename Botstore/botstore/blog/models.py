from django.db import models
from ckeditor.fields import RichTextField  # Correct field import for django-ckeditor


class Post(models.Model):
    """
    Model representing a blog post.
    """

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200, help_text="The title of the blog post.")
    content = RichTextField(
        config_name="extends", blank=True, help_text="The content of the blog post."
    )
    cover_image = models.ImageField(
        upload_to="blog_covers/",
        blank=True,
        null=True,
        help_text="Optional cover image for the blog post.",
    )
    published_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )  # Status field

    def __str__(self):
        return self.title
