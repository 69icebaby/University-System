from django.contrib import admin

from .models import Announcement, Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "recipient",
        "is_read",
        "created_at",
    )
    list_filter = (
        "is_read",
        "created_at",
    )
    search_fields = (
        "title",
        "message",
        "recipient__username",
    )
    list_editable = ("is_read",)
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_by",
        "is_published",
        "created_at",
    )
    list_filter = (
        "is_published",
        "created_at",
    )
    search_fields = (
        "title",
        "body",
        "created_by__username",
    )
    list_editable = ("is_published",)
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"
