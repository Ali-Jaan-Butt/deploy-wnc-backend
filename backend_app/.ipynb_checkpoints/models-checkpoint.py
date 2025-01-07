from django.db import models

class Signup_data(models.Model):
    joinas = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    pwd = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Student_data(models.Model):
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True, default='None')
    cnic = models.CharField(max_length=200, unique=True, default='None')
    phone = models.CharField(max_length=200, default='None')
    skills = models.TextField(default=[])
    description = models.CharField(max_length=2000, default='No description')
    profile = models.CharField(max_length=200, default='None')
    institute = models.CharField(max_length=200, default='None')
    inst_email = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.email

class Supervisor_data(models.Model):
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True, default='None')
    cnic = models.CharField(max_length=200, unique=True, default='None')
    phone = models.CharField(max_length=200, default='None')
    skills = models.TextField(default=[])
    description = models.CharField(max_length=2000, default='No description')
    profile = models.CharField(max_length=200, default='None')
    institute = models.CharField(max_length=200, default='None')
    inst_email = models.CharField(max_length=200, unique=True)
    designation = models.CharField(max_length=200, default='None')

    def __str__(self):
        return self.email

class Company_data(models.Model):
    email = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True, default='None')
    cnic = models.CharField(max_length=200, unique=True, default='None')
    phone = models.CharField(max_length=200, default='None')
    join_as = models.CharField(max_length=200, default='None')
    description = models.CharField(max_length=2000, default='No description')
    profile = models.CharField(max_length=200, default='None')
    org_name = models.CharField(max_length=200, default='None')
    org_website = models.CharField(max_length=200, default='None')
    location = models.CharField(max_length=200, default='None')

    def __str__(self):
        return self.email