from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def __str__(self):
        return self.as_p()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'email',
                                                  'id': 'floatingInput',
                                                  'placeholder': 'name@example.com',
                                                  'for': 'floatingInput'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'email',
                                                      'id': 'floatingPassword',
                                                      'placeholder': '******',
                                                      'for': 'floatingPassword',
                                                      })
        self.fields['password2'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'email',
                                                      'id': 'floatingPassword',
                                                      'placeholder': '******',
                                                      'for': 'floatingPassword'})

# class AuthUser(AuthenticationForm):

