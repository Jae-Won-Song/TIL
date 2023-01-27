# board/forms.py
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        # exclude = ('user', )


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        min_length=2, max_length=200,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    class Meta:
        model = Comment
        # fields = ('content', )
        exclude = ('article', 'user',)
