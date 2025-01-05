from django.db import models


class Signup_data(models.Model):
    joinas = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    pwd = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Student_db(models.Model):
    username = models.CharField(max_length=200, unique=True)
    cnic = models.CharField(max_length=200, unique=True, default='None')
    phone = models.CharField(max_length=200, default='None')
    description = models.TextField()
    profile = models.ImageField(upload_to='student_images/', null=True, blank=True)
    degree = models.CharField(max_length=200, default='None')
    major = models.CharField(max_length=200, default='None')
    semester = models.CharField(max_length=200, default='None')
    institute = models.CharField(max_length=200, default='None')
    email = models.CharField(max_length=200, default='None', unique=True)
    university_email = models.CharField(max_length=200, default='None', unique=True)
    skills = models.TextField(default=[])

    def __str__(self):
        return self.email


class Client_db(models.Model):
    username = models.CharField(max_length=200, unique=True)
    cnic = models.CharField(max_length=200, unique=True, default='None')
    phone = models.CharField(max_length=200, default='None')
    description = models.TextField()
    profile = models.ImageField(upload_to='client_images/', null=True, blank=True)
    joiningType = models.CharField(max_length=200, default='None')
    email = models.CharField(max_length=200, unique=True, default='None')
    organizationName = models.CharField(max_length=200, default='None')
    organizationEmail = models.CharField(max_length=200, unique=True, default='None')

    def __str__(self):
        return self.email


class Supervisor_db(models.Model):
    username = models.CharField(max_length=200, unique=True)
    cnic = models.CharField(max_length=200, unique=True, default='None')
    phone = models.CharField(max_length=200, default='None')
    description = models.TextField()
    profile = models.ImageField(upload_to='supervisor_images/', null=True, blank=True)
    designation = models.CharField(max_length=200, default='None')
    department = models.CharField(max_length=200, default='None')
    email = models.CharField(max_length=200, unique=True, default='None')
    institute = models.CharField(max_length=200, default='None')
    university_email = models.CharField(max_length=200, unique=True, default='None')
    skills = models.TextField(default=[])

    def __str__(self):
        return self.email

