from django.db import models

# Create your models here.
class faculties(models.Model): 
    student_number = models.PositiveIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    # phone_number = models.PositiveIntegerField()
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()

    def __str__(self):
        return self.first_name + " " + self.last_name
