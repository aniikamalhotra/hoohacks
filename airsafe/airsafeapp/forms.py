from django import forms

class inputForm(forms.Form):
    time = forms.CharField(max_lenth=10, default=0)
    volume = forms.CharField(max_length=10, default=0)