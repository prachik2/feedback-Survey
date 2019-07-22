from django.contrib import admin
from base_app.models import StudentCourseRegistration, SemesterOffering, Course, Student

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(SemesterOffering)
admin.site.register(StudentCourseRegistration)
