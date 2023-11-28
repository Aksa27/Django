from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    
class employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)