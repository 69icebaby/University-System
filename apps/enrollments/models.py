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

    # Ссылаемся на стандартного пользователя (или StudentProfile, в зависимости от вашей архитектуры accounts)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    # Связь с моделью Course из приложения courses
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    status: str = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Уникальный индекс для пары студент-курс из схемы DBML
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course_enrollment')
        ]

    def __str__(self) -> str:
        return f"{self.student} - {self.course} ({self.status})"


class Schedule(models.Model):
    class DayOfWeek(models.IntegerChoices):
        MONDAY = 1, 'Monday'
        TUESDAY = 2, 'Tuesday'
        WEDNESDAY = 3, 'Wednesday'
        THURSDAY = 4, 'Thursday'
        FRIDAY = 5, 'Friday'
        SATURDAY = 6, 'Saturday'

    # Связь расписания с курсом
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    day_of_week: int = models.IntegerField(choices=DayOfWeek.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom: str = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.course} | Day: {self.day_of_week} | {self.start_time}-{self.end_time}"