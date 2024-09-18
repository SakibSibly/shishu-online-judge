from django import forms


class UserRegistrationForm(forms.Form):
    name = forms.CharField(
        required=True,
        label='Name',
        widget=forms.TextInput(attrs={
            'placeholder': 'name'
        })
        )
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={
            'placeholder': 'username'
        })
        )
    email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'example@email.com'
        })
        )
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput)
    country = forms.CharField(required=True, label='Country')
    city = forms.CharField(required=True, label='City')
    institution = forms.CharField(required=True, label='Institution')
