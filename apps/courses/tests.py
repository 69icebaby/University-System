
from django.test import TestCase

from .models import CourseCategory


class CourseCategoryTest(TestCase):
    def test_category_creation(self):
        category = CourseCategory.objects.create(
            name="Programming",
            description="Programming courses",
        )

        self.assertEqual(category.name, "Programming")
        self.assertEqual(str(category), "Programming")
