from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__()

    username = UsernameField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
        }
        )
    )
    password = forms.CharField(
        max_length=50,
        label='Password',
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
            }
        )
    )
    email = forms.CharField(
        max_length=50,
        label='Email',
        widget=forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
            }
        )
    )
    password1 = forms.CharField(
        max_length=50,
        label='Password',
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
            }
        )
    )
    password2 = forms.CharField(
        max_length=50,
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form'}),
            'email': forms.TextInput(attrs={'class': 'form'})
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
