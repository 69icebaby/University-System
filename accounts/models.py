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
    student_id = models.CharField(
        max_length=20,
        unique=True,
    )
    faculty = models.CharField(max_length=100)
    year_of_study = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        full_name = self.user.get_full_name()

        if full_name:
            return f"{full_name} ({self.student_id})"

        return f"{self.user.username} ({self.student_id})"


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
    )
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.user.get_full_name() or self.user.username