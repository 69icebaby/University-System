from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "Student"
        TEACHER = "teacher", "Teacher"
        ADMIN = "admin", "Admin"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    def __str__(self) -> str:
        return self.username


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    student_number = models.CharField(
        max_length=30,
        unique=True,
    )
    department = models.CharField(max_length=150)
    enrollment_year = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.student_number} - {self.user.username}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
    )
    employee_number = models.CharField(
        max_length=30,
        unique=True,
    )
    department = models.CharField(max_length=150)
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.employee_number} - {self.user.username}"