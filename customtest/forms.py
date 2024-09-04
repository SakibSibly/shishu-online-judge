from django import forms


class CodeSubmissionForm(forms.Form):
    LANGUAGE_CHOICES = [
        ('0', 'GNU GCC 9.4.0'),
        ('1', 'GNU G++ 9.4.0'),
        ('2', 'Python 3.10.5'),
    ]
    code = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'distance',
            'cols': 100,
            'rows': 20,
            'id': 'code'
        })
    )
    input_data = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'distance',
            'cols': 30,
            'rows': 10,
            'id': 'stdinput'
        })
    )
    language = forms.ChoiceField(
        choices=LANGUAGE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'distance',
            'id': 'language'
        })
    )
