from django.db import models
from django.db.models.constraints import CheckConstraint
from django.db.models.query_utils import Q
from django.utils import timezone
from django.contrib.auth.models import User
import uuid  # Required for unique production actual instances
from datetime import date

class Shift(models.Model):
    shift_number = models.IntegerField()
    shift_name = models.CharField(max_length=15)
    def __str__(self):
        return self.shift_name

class Department(models.Model):
    department_name = models.CharField(max_length=40)
    def __str__(self):
        return self.department_name

class AssemblyLine(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    line_name = models.CharField(max_length=6)
    def __str__(self):
        return self.line_name

class Product(models.Model):
    assembly_line = models.ForeignKey(AssemblyLine, on_delete=models.CASCADE)
    PartNumber = models.CharField(max_length=15)
    TeamMember = models.CharField(max_length=2)
    CycleTime = models.CharField(max_length=4)
    ToteQuantity = models.IntegerField(default=0)
    class Meta:
        ordering = ['assembly_line', 'PartNumber', 'TeamMember', 'CycleTime']
    def __str__(self):
        #return '{0}{1}({2}){3}'.format(self.assembly_line, self.PartNumber, self.TeamMember, self.CycleTime)
        return '{1}'.format(self.assembly_line, self.PartNumber, self.TeamMember, self.CycleTime)

class ProductionActual(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular ProductionActual")
    pa_date = models.DateField('production actual date')
    assembly_line_number = models.ForeignKey(AssemblyLine, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{0} // ({1}) // {2} // {3} // {4}'.format(self.id, self.pa_date, self.assembly_line_number, self.shift, self.user)

class Hourly(models.Model):
    ProductionActual = models.OneToOneField(ProductionActual, primary_key=True, on_delete=models.CASCADE)
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
    def __str__(self):
        return '{0}'.format(self.ProductionActual)

class Run(models.Model):
    ProductionActual = models.ForeignKey(ProductionActual, on_delete=models.CASCADE)
    number = models.IntegerField(default=1, help_text="Run Number")
    partal_start = models.IntegerField(default=0, help_text="Start Partal quanity")
    partal_end = models.IntegerField(default=0, help_text="End Partal quanity")
    finished_goods = models.IntegerField(default=0, help_text="How many totes completed")
    kanban_count = models.IntegerField(default=0, help_text="How many Kanbans in post for current shift")
    product_number = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True, null=True)
    finish_time = models.TimeField(blank=True, null=True)
    plan_down_time = models.IntegerField(default=0)
    net_ope_time = models.IntegerField(default=0)
    plan_quanity = models.IntegerField(default=0)
    result_quanity = models.IntegerField(default=0)
    scrap_quanity = models.IntegerField(default=0)
    repair_quanity = models.IntegerField(default=0)
    analysis_quanity = models.IntegerField(default=0)
    quarantine_quanity = models.IntegerField(default=0)
    cabbage_patch_quanity = models.IntegerField(default=0)
    unplan_downtime = models.IntegerField(default=0)
    standard_time = models.IntegerField(default=0)
    oa = models.IntegerField(default=0)
    oa_without_downtime = models.IntegerField(default=0)
    class Meta:
            constraints = [
                models.UniqueConstraint(
                    fields=['ProductionActual', 'number'], 
                    name='unique number'
                )
            ]
            
    def __str__(self):
        return 'Run: {0} + {1} '.format(self.number, self.ProductionActual)
        #return self.ProductionActual

    ## origional run constraints
    # class Meta:
    #         constraints = [
    #             models.UniqueConstraint(
    #                 fields=['ProductionActual', 'number'], 
    #                 name='unique number'
    #             )
    #         ]

class Machine(models.Model):
    assembly_line = models.ForeignKey(AssemblyLine, on_delete=models.CASCADE)
    machine_name = models.CharField(max_length=40)
    machine_name_short = models.CharField(max_length=5)
    machine_name_actual = models.CharField(max_length=7)
    def __str__(self):
        return self.machine_name_short

class Defect(models.Model):
    assembly_line = models.ForeignKey(AssemblyLine, on_delete=models.CASCADE)
    FourM =  models.CharField(max_length=7)
    Machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    defect_code = models.CharField(max_length=10)
    defect_description = models.CharField(max_length=50)
    def __str__(self):
        return self.defect_code

class DefectInstance(models.Model):
    ProductionActual = models.ForeignKey(ProductionActual, on_delete=models.CASCADE)
    production_run = models.ForeignKey(Run, default=1, on_delete=models.CASCADE)
    defect = models.ForeignKey(Defect, on_delete=models.CASCADE)
    defect_quanity = models.IntegerField(default=1)

class Downtime(models.Model):
    assembly_line = models.ForeignKey(AssemblyLine, on_delete=models.CASCADE)
    Machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    FourM =  models.CharField(max_length=7)
    downtime_code = models.CharField(max_length=5)
    planned = models.BooleanField(default=False)
    default_recovery_time = models.FloatField(max_length=7, default=0.0, help_text="how long of downtime")
    downtime_description = models.CharField(max_length=50)
    def __str__(self):
        return self.downtime_code

class DowntimeInstance(models.Model):
    ProductionActual = models.ForeignKey(ProductionActual, on_delete=models.CASCADE)
    production_run = models.ForeignKey(Run,default=1, on_delete=models.CASCADE)
    downtime = models.ForeignKey(Downtime, on_delete=models.CASCADE)
    recovery_time = models.FloatField(max_length=7, help_text="how long of downtime")
    occurrence_multiplier = models.IntegerField(default=1, help_text="how many times did this happen")
