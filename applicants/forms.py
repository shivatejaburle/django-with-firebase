from django import forms
from django.conf import settings

class SignInForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(strip=False, widget=forms.PasswordInput)

class ResetPasswordForm(forms.Form):
    email = forms.EmailField(max_length=150)

from os.path import join
class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    phone = forms.CharField(max_length=20)
    file = forms.FileField(label="Please upload your file")