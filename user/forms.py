from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Username'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your Password'
        })
        self.fields['username'].label = ''
        self.fields['password'].label = ''


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Name'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Re-enter Password'
        })


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'DOB', 'type']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date', 'class': "date-picker", "style": "max-width: 200px;"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].widget.attrs.update({
            'style': 'display: none'
        })
        self.fields['profile_pic'].widget.attrs.update({
            'onchange': 'imageUpload(event)'
        })
