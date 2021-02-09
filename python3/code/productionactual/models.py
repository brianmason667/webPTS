from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
user = get_user_model()
from django.db import models

SHIFT_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Flex'),
]

class department(models.Model):
    department_name = models.CharField(max_length=40)
    def __str__(self):
        return self.department_name

class assembly_line(models.Model):
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    line_name = models.CharField(max_length=6)
    def __str__(self):
        return self.line_name

class productionactual_instance(models.Model):
    pa_date = models.DateTimeField('production actual date')
    assembly_line_number = models.ForeignKey(assembly_line, on_delete=models.CASCADE)
    shift = models.IntegerField(default=0, choices=SHIFT_CHOICES)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

class productionactual(models.Model):
    pa_date = models.DateTimeField('production actual date')
    assembly_line_number = models.ForeignKey(assembly_line, on_delete=models.CASCADE)
    shift = models.IntegerField(default=0, choices=SHIFT_CHOICES)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

class hourly(models.Model):
    productionactual = models.ForeignKey(productionactual, on_delete=models.CASCADE)
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

