from django import forms

class ContactForm(forms.Form):
    phone = forms.RegexField(label="Номер телефона",regex='^\+?3?8?(0[5-9][0-9]\d{7})$',error_messages={'invalid': 'Некоректно введен номер'})
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
