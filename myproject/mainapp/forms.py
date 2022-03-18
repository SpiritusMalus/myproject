from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def __str__(self):
        return self.as_p()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
