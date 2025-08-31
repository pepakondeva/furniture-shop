from django import forms
import re
from django.core.exceptions import ValidationError

# class ContactForm(forms.Form):
    # name = forms.CharField(label='Вашето име', max_length=100)
    # email = forms.EmailField(label='Имейл')
    # number = forms.CharField(label='Телефон за връзка')
    # message = forms.CharField(label='Съобщение', widget=forms.Textarea)

def clean_number(self):
    number = self.cleaned_data['number']
    pattern = r'^(\+359|0)[87][0-9]{8}$'
    if not re.match(pattern, number):
        raise ValidationError('Моля, въведете валиден български телефонен номер.')
    return number


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Вашето име',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Въведете вашето име'
        })
    )

    email = forms.EmailField(
        label='Имейл',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@email.com'
        })
    )

    number = forms.CharField(
        label='Телефон за връзка',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+359 88 123 4567'
        })
    )

    message = forms.CharField(
        label='Съобщение',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Напишете вашето съобщение...'
        })
    )

