import datetime
from django.forms import ModelForm, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from .models import CustomUser
from .models import Projects, Requests
from django.utils.timezone import now


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


class ProjectCreationForm(forms.ModelForm):
    preview = forms.ImageField()
    title = forms.CharField(
        label="Title",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
        }
        )
    )
    text = forms.CharField(
        label="Text",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
        }
        )
    )
    created_date = forms.DateTimeField(
        initial=datetime.date.today(),
        widget=forms.HiddenInput,
    )
    author = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.HiddenInput()
    )
    likes = forms.IntegerField(
        widget=forms.HiddenInput,
        initial=0
    )

    class Meta:
        model = Projects
        fields = "__all__"


class RequestLeaveForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.HiddenInput()
    )
    text = forms.CharField(
        label="Text",
        widget=Textarea(attrs={"maxlength": "500",
                               'class': 'form-control',
                               }
                        )
    )
    phone = forms.CharField(
        label='Phone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_phone',
            }
        ),
    )
    sending_date = forms.DateTimeField(
        initial=datetime.date.today(),
        widget=forms.HiddenInput,
    )

    class Meta:
        model = Requests
        fields = "__all__"
