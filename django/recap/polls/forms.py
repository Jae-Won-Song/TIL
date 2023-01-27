from django import forms
from .models import Question, Reply

class QuestionForm(forms.ModelForm):
    title = forms.CharField(min_length=3, max_length=200)
    class Meta:
        model = Question
        # 모든 필드(title,user)들 중 아래 필드만 HTML에 보여주고 검증함
        fields = ('title',)


class ReplyForm(forms.ModelForm):
    content = forms.CharField(min_length=3, max_length=200)
    class Meta:
        model = Reply
        fields = ('content',)