from django import forms

class inputForm(forms.Form):
    time = forms.FloatField()
    volume = forms.FloatField()

    class Meta:
        fields = ['time', 'volume']