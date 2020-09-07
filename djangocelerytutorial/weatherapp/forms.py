from django import forms
from .tasks import task_get_weather


class CityForm(forms.Form):
    city = forms.CharField(label='City', max_length=30, required=True)
    honeypot = forms.CharField(widget=forms.HiddenInput(), required=False)

    def get_weather_data(self):
        if self.cleaned_data['honeypot']:
            return False
        task_get_weather.delay(self.cleaned_data['city'])
