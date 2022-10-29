from django import forms
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()


class UploadForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # file = forms.FileField()
    class Meta:
        model = Product
        # user = User
        # user = request.user.username
        fields = "__all__"
        exclude = ['id']
        # fields = ['product_name', 'price', 'category', 'expected_sales_date', 'current_bid', 'images', 'details']

        

class updateform(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['id', 'poster']