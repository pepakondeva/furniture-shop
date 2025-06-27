from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Вашето име', max_length=100)
    email = forms.EmailField(label='Имейл')
    number = forms.CharField(label='Телефон за връзка')
    message = forms.CharField(label='Съобщение', widget=forms.Textarea)
