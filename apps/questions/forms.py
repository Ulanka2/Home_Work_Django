from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('contact', 'question')
        
        widgets = {
        'contact': forms.TextInput(attrs={'class':'form-control'}),
        'question': forms.Textarea(attrs={'class':'form-control'}),
        }