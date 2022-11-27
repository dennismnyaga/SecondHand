from django import forms
from frontend.models import *
from users.models import *




class statusform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['status']