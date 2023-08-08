from django import forms
from newa.models import *

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
