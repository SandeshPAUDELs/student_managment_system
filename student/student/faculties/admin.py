from django.contrib import admin

# Register your models here.
from .models import faculties
# admin.site.register(faculties)
class facultiesAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa')

admin.site.register(faculties, facultiesAdmin)