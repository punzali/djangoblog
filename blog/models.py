
from django.db import models
from django.conf import settings
from django.utils.text import slugify

from PIL import Image


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts"
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="published"
    )

    cover_image = models.ImageField(
        upload_to="posts/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        # Generate a unique slug for new posts
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        # Save the post
        super().save(*args, **kwargs)

        # Resize uploaded image
        if self.cover_image:
            img_path = self.cover_image.path

            img = Image.open(img_path)

            if img.height > 800 or img.width > 800:
                img.thumbnail((800, 800))
                img.save(img_path)
