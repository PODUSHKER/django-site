import uuid
from datetime import timedelta

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.utils.timezone import now

from users.models import *

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder':"Введите имя пользователя"
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder':"Введите пароль"
    }))
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите имя пользователя"
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите пароль"
    }))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите имя"
    }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите фамилию"
    }))
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Введите адрес эл. почты"
    }))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={
        'class': "form-control py-4",
        'placeholder': "Подтвердите пароль"
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        obj = super().save(commit=True)
        time_to_die = now() + timedelta(minutes=600)
        mail = EmailVerifyMessage.objects.create(user=obj, uuid=uuid.uuid4(), time_to_die=time_to_die)
        mail.send_verify_message()
        return obj

class ProfileForm(UserChangeForm):

    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': "form-control py-4",
    }))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': "form-control py-4",
    }))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': "form-control py-4",
    }))
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={
        'class': "form-control py-4",
    }))
    image = forms.FileField(required=False, label='Фото', widget=forms.FileInput(attrs={
        'class': '"custom-file-input"'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'image']