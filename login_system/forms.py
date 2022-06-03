from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import AuthenticationForm
import re


# Create your models here.


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['password2', 'username', 'password1']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['type'] = 'email'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

        self.fields['password1'].widget.attrs['type'] = 'password'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['type'] = 'password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['type'] = 'username'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'

        self.fields['password'].widget.attrs['type'] = 'password'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class SendEmailForm(forms.Form):
    to = forms.EmailField()
    subject = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ['to', 'subject', 'content']

    def __init__(self, *args, **kwargs):
        super(SendEmailForm, self).__init__(*args, **kwargs)

        self.fields['to'].widget.attrs['type'] = 'email'
        self.fields['to'].widget.attrs['class'] = 'form-control'
        self.fields['to'].widget.attrs['placeholder'] = 'name@example.com'

        self.fields['subject'].widget.attrs['class'] = 'form-control'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'

        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['row'] = '5'
        self.fields['content'].widget.attrs['style'] = 'resize:none;'

