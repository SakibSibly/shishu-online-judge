from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)


class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True, label='Username')
    email = forms.EmailField(required=True, label='Email')
    password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, label='Confirm Password', widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, label='First Name')
    last_name = forms.CharField(required=True, label='Last Name')
    country = forms.CharField(required=True, label='Country')
    city = forms.CharField(required=True, label='City')
    institution = forms.CharField(required=True, label='Institution')
