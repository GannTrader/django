from django import forms
from .models import Post, Catagory

choices = Catagory.objects.all().values_list('name', 'name')
# choices = [('coding', 'coding'), ('sport', 'sport'), ('entertainment', 'entertainment')]
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'catagory', 'body')

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "title_tag": forms.TextInput(attrs={'class': 'form-control'}),
            "author": forms.TextInput(attrs={'class': 'form-control', 'id': 'quyduong', 'value': ''}),
            # "author": forms.Select(attrs={'class': 'form-control'}),
            "catagory": forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            "body": forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'catagory', 'body')

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "title_tag": forms.TextInput(attrs={'class': 'form-control'}),
            "catagory": forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            # "author": forms.Select(attrs={'class': 'form-control'}),
            "body": forms.Textarea(attrs={'class': 'form-control'}),
        }