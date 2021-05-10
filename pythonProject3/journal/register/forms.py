from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class UserReg(UserCreationForm):
    username = forms.CharField(label='Логин*',
                               help_text='Введите логин',
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите логин'}))
    email = forms.EmailField(required=False,
                            label='Email',
                            help_text='Введите Ваш email',
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Введите email'}))
    password1 = forms.CharField(required=True,
                               label='Пароль*',
                               help_text='Пароль не должен быть сильно простым',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(required=True,
                                label='Подтверждение пароля*',
                                help_text='Для подтверждения повторно введите Ваш пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Введите пароль'}))

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']


class ImageChange(forms.ModelForm):
    img = forms.ImageField(label="Фото",
                           required=False,
                           widget=forms.FileInput)

    class Meta:
        model = Profile
        fields = ['img']

class UserChange(forms.ModelForm):
    username = forms.CharField(label="Логин",
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.CharField(label="Email",
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']