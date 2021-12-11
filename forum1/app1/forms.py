from django import forms
from .models import CommentData

class CommentDataForm(forms.ModelForm):
    class Meta:
        model = CommentData
        fields = '__all__'