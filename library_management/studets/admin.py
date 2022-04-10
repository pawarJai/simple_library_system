from django.contrib import admin
from .models import CourceDepartment,Student

# Register your models here.


@admin.register(CourceDepartment)
class CourceDepartmentAdmin(admin.ModelAdmin):
    list_display = ["id","label"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id","student_first_name","student_last_name","enrollment_no","cource_department","created_at"]