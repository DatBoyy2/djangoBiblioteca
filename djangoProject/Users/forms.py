from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import User


class LoginForm(forms.Form):

    email = forms.CharField(
        label ="Email",
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Email'
            }
        )
    )

    password= forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'**'
            }
        )
    )

    def clean(self):
        self.cleaned_data= super(LoginForm, self).clean()
        email= self.cleaned_data['email']
        password=self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Incorrect data')

        return self.cleaned_data

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name', 'surname']

    def clean_password2 (self):
        if self.cleaned_data.get('password') !=  self.cleaned_data['password2']:
            self.add_error('password2', 'Passwords do not match')