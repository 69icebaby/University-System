from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import StudentProfile, TeacherProfile, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "University information",
            {
                "fields": ("role",),
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "University information",
            {
                "fields": ("role",),
            },
        ),
    )

    actions = (
        "activate_users",
        "deactivate_users",
    )

    @admin.action(description="Activate selected users")
    def activate_users(self, request, queryset) -> None:
        queryset.update(is_active=True)

    @admin.action(description="Deactivate selected users")
    def deactivate_users(self, request, queryset) -> None:
        queryset.update(is_active=False)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "user",
        "faculty",
        "year_of_study",
    )

    search_fields = (
        "student_id",
        "user__username",
        "user__first_name",
        "user__last_name",
    )

    list_filter = (
        "faculty",
        "year_of_study",
    )


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "department",
        "position",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "department",
    )

    list_filter = (
        "department",
        "position",
    )