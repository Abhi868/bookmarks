

from django import forms

from django.contrib.auth.models  import User

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput, max_length=40)


class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(max_length=40, label='Password', widget=forms.PasswordInput)
    password2=forms.CharField(max_length=40 , label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','email']
    
    def clean_password(self):
        cd=self.cleaned_data
        if cd['password']!= cd['password2']:
            raise forms.ValidationError('Passwod didn\'t match')
        return cd['password2']

