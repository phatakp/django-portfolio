from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Your Name"}))

    email = forms.CharField(
        widget=forms.EmailInput(attrs={"placeholder": "Your Email Address"})
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Message", "rows": 4})
    )

    class Meta:
        model = Contact
        fields = "__all__"
