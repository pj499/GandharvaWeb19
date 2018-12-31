from django import forms
from django.contrib.auth.models import User
from .models import ContactUs

class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','password']


class ContactUsForm(forms.ModelForm):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True,widget=forms.Textarea)

    class Meta:
        model = ContactUs
        fields = ['user_name','user_id','user_message']





