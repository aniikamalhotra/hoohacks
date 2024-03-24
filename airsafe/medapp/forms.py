from django import forms

class inputForm(forms.Form):
    time = forms.FloatField()
    diameter = forms.FloatField()

    class Meta:
        fields = ['time', 'diameter']