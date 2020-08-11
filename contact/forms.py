from .models import Conatct
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Enter Username', label_suffix='-->',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Enter Password", label_suffix='-->',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = '__all__'


class SignupForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', label_suffix='-->',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    first_name = forms.CharField(label='Enter FirstName', label_suffix='-->',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(label='Enter LastName', label_suffix='-->',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label="Enter Email", label_suffix="-->",
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label="Enter Password", label_suffix='-->',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label="conform Password", label_suffix='-->',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Conatct
        exclude = ['contact_of']
        labels = {'name': 'Enter Name',
                  'phone': 'Enter Phone',
                  'email': 'Enter Email'}

        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'})}
