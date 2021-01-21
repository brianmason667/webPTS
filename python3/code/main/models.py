import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class users(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
    username = models.CharField(max_length=40)
    def __str__(self):
        return self.username
    email = models.CharField(max_length=40)
    def __str__(self):
        return self.email
    password = models.CharField(max_length=40)
    def __str__(self):
        return self.password
    create_datetime = models.DateTimeField('account create date')
    isadmin = models.IntegerField(default=0)

class departments(models.Model):
    department_name = models.CharField(max_length=40)
    def __str__(self):
        return self.department_name

class assembly_lines(models.Model):
    departments = models.ForeignKey(departments, on_delete=models.CASCADE)
    line_names = models.CharField(max_length=6)
    def __str__(self):
        return self.line_names

class pauid(models.Model):
    pa_date = models.DateTimeField('production actual date')
    assembly_line_number = models.ForeignKey(assembly_lines, on_delete=models.CASCADE)
    shift = models.IntegerField(default=0)
    userid = models.ForeignKey(users, on_delete=models.CASCADE)
    def __str__(self):
        return self.assembly_line_number



class Choice(models.Model):
    question = models.ForeignKey(pauid, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class hourly(models.Model):
    pauid = models.ForeignKey(pauid, on_delete=models.CASCADE)
    hour1 = models.IntegerField(default=0)
    hour2 = models.IntegerField(default=0)
    hour3 = models.IntegerField(default=0)
    hour4 = models.IntegerField(default=0)
    hour5 = models.IntegerField(default=0)
    hour6 = models.IntegerField(default=0)
    hour7 = models.IntegerField(default=0)
    hour8 = models.IntegerField(default=0)
    hour9 = models.IntegerField(default=0)
    hour10 = models.IntegerField(default=0)
    hour11 = models.IntegerField(default=0)
    hour12 = models.IntegerField(default=0)