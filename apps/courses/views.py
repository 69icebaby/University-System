
from django.http import JsonResponse


def courses_home(request):
    return JsonResponse({
        "message": "Courses app is working",
    })