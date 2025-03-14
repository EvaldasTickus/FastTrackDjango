from django import forms
from django.forms import ModelForm
from .models import City


class NameForm(forms.Form):
    city = forms.CharField(label='City', max_length=100, min_length="3")
    country = forms.CharField(label='Country', max_length=100, min_length="3")
    coordination_x = forms.CharField(label='coordination_x')
    coordination_y = forms.CharField(label='coordination_y')

# class CityForm(ModelForm):
#
#     class Meta:
#         model = City
#         fields = "_a_all__"
