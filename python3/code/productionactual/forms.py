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
