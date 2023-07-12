from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input-field'
            field.widget.attrs['placeholder'] = field.label


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input-field'
            field.widget.attrs['placeholder'] = field.label