from django.db import models

# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=300)

class User(models.Model):
    fullname = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
