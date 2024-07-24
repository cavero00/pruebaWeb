from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'imporant']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            #'imporant': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'imporant': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }