import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.utils.translation import ugettext_lazy as _
from .models import *

class NewProductionActualForm(forms.ModelForm):
    pa_date = forms.DateField(widget=forms.DateInput)
    class Meta:
        model = ProductionActual
        fields = [
            "pa_date",
            "assembly_line_number",
            "shift",
        ]

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "assembly_line",
            "PartNumber",
            "TeamMember",
            "CycleTime",
        ]

class HourlyForm(forms.ModelForm):
    class Meta:
        model = Hourly
        fields = [
            "hour1",
            "hour2",
            "hour3",
            "hour4",
            "hour5",
            "hour6",
            "hour7",
            "hour8",
            "hour9",
            "hour10",
            "hour11",
            "hour12",
        ]

class RunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = [
            "number",
            "partal_start",
            "partal_end",
            "finished_goods",
            "kanban_count",
            "product_number",
            "start_time",
            "finish_time",
            "plan_down_time",
            "net_ope_time",
            "plan_quanity",
            "result_quanity",
            "scrap_quanity",
            "repair_quanity",
            "analysis_quanity",
            "quarantine_quanity",
            "cabbage_patch_quanity",
            "unplan_downtime",
            "standard_time",
            "oa",
            "oa_without_downtime",
        ]

class NewRunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = [
            "partal_start",
            "partal_end",
            "finished_goods",
            "kanban_count",
            "product_number",
            "start_time",
            "finish_time",
        ]

class EditRunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = [
            "number",
            "partal_start",
            "partal_end",
            "finished_goods",
            "kanban_count",
            "product_number",
            "start_time",
            "finish_time",
        ]

class RemoveRunForm(forms.ModelForm):
    class Meta:
        model = Run
        fields = [
            
        ]