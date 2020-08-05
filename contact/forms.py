from .models import Conatct
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Conatct
        fields = '__all__'
        labels = {'name': 'Enter Name',
                  'phone': 'Enter Phone',
                  'email': 'Enter Email'}
                  
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'})}
