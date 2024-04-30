from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



