from django.contrib import admin

# Register your models here.
from App1.models import students,employee
admin.site.register(students)
admin.site.register(employee)