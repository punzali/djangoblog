
from django.contrib import admin
from django.utils.html import format_html

from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "cover_image_preview",
        "status",
        "created_at",
    )

    list_filter = ("status",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}

    def cover_image_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" width="100" height="70" '
                'style="object-fit: cover; border-radius: 6px;" />',
                obj.cover_image.url,
            )
        return "No cover image"

    cover_image_preview.short_description = "Cover Image"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
