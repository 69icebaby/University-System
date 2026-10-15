from django.contrib import admin

from .models import Announcement, Notification, NotificationPreference


@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "email_enabled",
        "assignment_alerts",
        "grade_alerts",
    )
    list_filter = (
        "email_enabled",
        "assignment_alerts",
        "grade_alerts",
    )
    search_fields = ("user__username",)
    list_editable = (
        "email_enabled",
        "assignment_alerts",
        "grade_alerts",
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "course",
        "is_published",
        "created_at",
    )
    list_filter = (
        "is_published",
        "created_at",
    )
    search_fields = (
        "title",
        "content",
        "author__username",
    )
    list_editable = ("is_published",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "recipient",
        "notification_type",
        "course",
        "assignment",
        "is_read",
        "created_at",
    )
    list_filter = (
        "notification_type",
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
