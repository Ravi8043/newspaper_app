from django import forms
from .models import ArticlesModel


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = ArticlesModel
        fields = ['title','content','created_by',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'created_by': 'Created By',
        }