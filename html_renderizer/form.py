from django import forms
from .models import Generated_Html


# forms.py
from django import forms
from .models import Generated_Html

class Generated_Html_Form(forms.ModelForm):
    class Meta:
        model = Generated_Html
        fields = ['title', 'prompt', 'html_code', 'ai']
        labels = {
            'title': 'Title',
            'prompt': 'Prompt',
            'html_code': 'HTML Code',
            'ai': 'Select AI',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'prompt': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'html_code': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'ai': forms.Select(attrs={'class': 'form-control'}),
        }

