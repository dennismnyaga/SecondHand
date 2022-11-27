from django import forms
from tinymce.widgets import TinyMCE
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()


class UploadForm(forms.ModelForm):
    details = forms.CharField(
        widget=TinyMCE(attrs={"cols": 80, "rows": 15, "class": "form-control"})
    )
    
    class Meta:
        model = Product
        
        fields = "__all__"
        exclude = ['id', 'status']
        

        

class updateform(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['id', 'poster','status']