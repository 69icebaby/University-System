from django.db import models


class Assignment(models.Model):
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="assignments",
    )
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
