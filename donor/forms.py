from django import forms

# Create your forms here.


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    # mobile = forms.NumberInput(required=True)
    email_address = forms.EmailField(max_length=150, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Message', 'style': "width: 100%; height: 150px;"}),
        max_length=2000, required=True)
