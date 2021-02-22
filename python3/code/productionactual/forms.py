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