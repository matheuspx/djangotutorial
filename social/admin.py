from django.contrib import admin
from .models import Post, Like, Comment, Share


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "created_at")
    search_fields = ("content", "author__username")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    list_per_page = 20


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    search_fields = ("user__username", "post__content")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content", "created_at")
    search_fields = ("content", "user__username", "post__content")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    search_fields = ("user__username", "post__content")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
