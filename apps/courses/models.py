
from django.conf import settings
from django.db import models


class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "courses_coursecategory"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Course(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        DRAFT = "DRAFT", "Draft"

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="courses",
        db_column="teacher_id",
    )

    category = models.ForeignKey(
        CourseCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
        db_column="category_id",
    )

    code = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    credits = models.PositiveIntegerField()
    semester = models.CharField(max_length=30, blank=True)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "courses_course"
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.title}"


class CourseMaterial(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="materials",
        db_column="course_id",
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.CharField(max_length=500, blank=True)
    material_type = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "courses_coursematerial"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.course.code} - {self.title}"
