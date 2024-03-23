from django import forms

class inputForm(forms.Form):
    time = forms.CharField(max_length=10)
    volume = forms.CharField(max_length=10)

    class Meta:
        fields = ['time', 'volume']