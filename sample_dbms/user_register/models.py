from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class User(models.Model):
    phone_number_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="You must enter a valid phone number (format: +99999999)"
    )
    fullname = models.CharField(max_length=200)
    emp_code = models.CharField(max_length=20)
    phone_number = models.CharField(validators=[phone_number_regex], max_length=20)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
