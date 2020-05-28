from django import forms
from django.utils import timezone

class Picker(forms.Form):
    date_start = forms.SplitDateTimeField()
    date_end = forms.SplitDateTimeField()
