from django import forms
from .models import Prompt

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ['request']  # Remove the 'ai' field from the form
        widgets = {
            'request': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
