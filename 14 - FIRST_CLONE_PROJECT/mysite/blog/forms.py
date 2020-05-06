from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'id':'exampleFormControlTextarea1', 'rows':'3'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }