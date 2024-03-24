from django import forms

class inputForm(forms.Form):
    time = forms.IntegerField()
    volume = forms.IntegerField()

    class Meta:
        fields = ['time', 'volume']