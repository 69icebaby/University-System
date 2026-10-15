from django.contrib import admin
from .models import Group, Enrollment, Schedule


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialty')
    search_fields = ('name', 'specialty')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'status', 'enrolled_at')
    list_filter = ('status', 'enrolled_at')
    search_fields = ('student__username', 'course__title')
    list_editable = ('status',)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('course', 'day_of_week', 'start_time', 'end_time', 'classroom')
    list_filter = ('day_of_week',)
    search_fields = ('course__title', 'classroom')