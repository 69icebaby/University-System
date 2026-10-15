from django.contrib import admin

from .models import Assignment, Grade, Submission, SubmissionFile


admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(SubmissionFile)
admin.site.register(Grade)
