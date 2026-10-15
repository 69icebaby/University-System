from django.db import models
from django.conf import settings


class Group(models.Model):
    name: str = models.CharField(max_length=50, unique=True)
    specialty: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Enrollment(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        REJECTED = 'rejected', 'Rejected'
        CANCELLED = 'cancelled', 'Cancelled'

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    # Временно закоменнтируем ссылку на Course, если приложения courses еще нет
    # course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='enrollments')
    course_name: str = models.CharField(max_length=100)  # Временное поле для названия курса
    status: str = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student} - {self.course_name} ({self.status})"


class Schedule(models.Model):
    class DayOfWeek(models.IntegerChoices):
        MONDAY = 1, 'Monday'
        TUESDAY = 2, 'Tuesday'
        WEDNESDAY = 3, 'Wednesday'
        THURSDAY = 4, 'Thursday'
        FRIDAY = 5, 'Friday'
        SATURDAY = 6, 'Saturday'

    # Временно закоментируем
    # course = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='schedules')
    course_name: str = models.CharField(max_length=100)
    day_of_week: int = models.IntegerField(choices=DayOfWeek.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom: str = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.course_name} | Day: {self.day_of_week} | {self.start_time}-{self.end_time}"