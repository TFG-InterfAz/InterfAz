from django import forms

class PromptForm(forms.Form):
    description = forms.CharField(
        label="Write here your request",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your prompt here'
        })
    )
