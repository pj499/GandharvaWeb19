from django import forms
from .models import ContactUs, MyUser

class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(max_length=75, required = True )
    class Meta:
        model = MyUser
        fields = ['username','email','password']


class ContactUsForm(forms.ModelForm):
    user_name = forms.CharField(required=True)
    user_id = forms.EmailField(required=True)
    category = forms.CharField(required=False)
    user_message = forms.CharField(required=True,widget=forms.Textarea)
    class Meta:
        model = ContactUs
        fields = ['user_name','user_id','user_message','category']



class HeadRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    user_type= forms.IntegerField()
    class Meta:
        model = MyUser
        fields = ['username','email','password','user_type']


