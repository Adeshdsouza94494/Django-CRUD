from django.db import models

# Create your models here.

class Student(models.Model):
    MY_CHOICES = [
        ("CE", 'Civil Engineering'),
        ("EXTC", 'Electronics and Telecommunication'),
        ("ME", 'Mechanical Engineering'),
        ("AI", 'Artificial Intelligence'),
        ("IT", 'Information Technology'),
    ]

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    branch = models.CharField(max_length=5, choices=MY_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
