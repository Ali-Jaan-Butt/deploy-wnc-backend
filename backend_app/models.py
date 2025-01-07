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




class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.message[:30]}"


class Jobs(models.Model):
    company_username = models.CharField(max_length=200)
    job_id = models.CharField(max_length=20, unique=True, editable=False)
    job_title = models.CharField(max_length=400)
    job_description = models.TextField()
    job_type = models.CharField(max_length=200)
    job_EndDate = models.TextField()
    job_budget = models.FloatField()
    job_duration = models.IntegerField()
    required_skills = models.JSONField(default=list)

    def __str__(self):
        return self.job_title


class Proposal(models.Model):
    job_id_id = models.ForeignKey(Jobs, to_field='job_id', on_delete=models.CASCADE, default='None')
    proposal_time = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=200)
    proposal_message = models.TextField()

    def __str__(self):
        return self.job_id_id


class Place_orders(models.Model):
    job_id_id = models.ForeignKey(Jobs, to_field='job_id', on_delete=models.CASCADE, default='None')
    user_name = models.CharField(max_length=200)
    order_time = models.DateTimeField(auto_now_add=True)
    budget = models.IntegerField()
    end_date = models.TextField()

    def __str__(self):
        return self.job_id_id
