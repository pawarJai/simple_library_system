from django.db import models
from my_library.models import User

# Create your models here.

class CourceDepartment(models.Model):
    label=models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Student(models.Model):
    student_first_name = models.CharField(max_length=120)
    student_last_name = models.CharField(max_length=120)
    enrollment_no  = models.IntegerField(unique=True)
    cource_department = models.ForeignKey(CourceDepartment,on_delete=models.CASCADE)
    student_id = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.student_first_name,"Enrollment no is ",self.enrollment_no)