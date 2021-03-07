import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if a date is not in the past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

SHIFT_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Flex'),
]

class NewProductionActualForm(forms.Form):
    pa_date = forms.DateField(required=False)
    name = forms.CharField(max_length=100)
    shift = forms.IntegerField(
        widget=forms.Select(choices=SHIFT_CHOICES),
    )
    line_name = forms.CharField(max_length=6)
    forms.ModelMultipleChoiceField
    
    
    # (queryset=line_name.objects.all())


# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())




# assembly_line_number = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

# forms.ForeignKey(assembly_line, on_delete=models.CASCADE)