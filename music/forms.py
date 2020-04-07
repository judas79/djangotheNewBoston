# L34 base user class, and form class, for forms
from django.contrib.auth.models import User
from django import forms

# L34 inheret from forms
class UserForm(forms.ModelForm):

    # specify that  a password will be used and pass in asterisks to mask it
    password = forms.CharField(widget=forms.PasswordInput)

    # Meta is information about the class that its within
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
