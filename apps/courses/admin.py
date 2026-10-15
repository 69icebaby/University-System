
from django.contrib import admin

from .models import Course, CourseCategory, CourseMaterial


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "title",
        "teacher",
        "category",
        "credits",
        "semester",
        "status",
    )
    list_filter = ("status", "category", "semester")
    search_fields = ("code", "title", "teacher__username")
    list_select_related = ("teacher", "category")


@admin.register(CourseMaterial)
class CourseMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "course",
        "material_type",
        "created_at",
    )
    list_filter = ("material_type",)
    search_fields = ("title", "course__code", "course__title")
    list_select_related = ("course",)
