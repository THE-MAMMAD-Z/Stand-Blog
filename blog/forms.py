from django import forms
from home.models import Contact
from .models import Comment

# class TestForm(forms.Form):
#     name=forms.CharField(max_length=180)
#     email=forms.EmailField()
#     subject=forms.CharField(max_length=250)
#     message=forms.CharField(widget=forms.Textarea)
    
class TestForm(forms.ModelForm):
    
    class Meta:
        model=Contact
        fields='__all__'
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model=Comment
        fields=['post','name','email','subject','message']
        
        
    