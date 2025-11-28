from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form_input'}),
            'message': forms.Textarea(attrs={'class': 'form_textarea'}),
        }