import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from django.utils.translation import ugettext_lazy as _
from .models import *

class NewProductionActualForm(forms.ModelForm):
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
            "AssemblyLine_ID",
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





# class HourlyForm(forms.Form):
#     hour1 = forms.IntegerField()
#     hour2 = forms.IntegerField()
#     hour3 = forms.IntegerField()
#     hour4 = forms.IntegerField()
#     hour5 = forms.IntegerField()
#     hour6 = forms.IntegerField()
#     hour7 = forms.IntegerField()
#     hour8 = forms.IntegerField()
#     hour9 = forms.IntegerField()
#     hour10 = forms.IntegerField()
#     hour11 = forms.IntegerField()
#     hour12 = forms.IntegerField()
   