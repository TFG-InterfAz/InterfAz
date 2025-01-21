from django import forms
from InterfAz.models import Prompt

class PromptForm(forms.ModelForm):
    class Meta:
        model = Prompt
        fields = ['request']  
        widgets = {
            'request': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
