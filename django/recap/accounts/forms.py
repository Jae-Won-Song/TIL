from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# models.py 에서 ForeignKey 가 User 일 때만, settings.AUTH_USER_MODEL
# 나머지 경우에 USER클래스가 필요하면, get_user_model()

User = get_user_model()


class CustomUserCreationFrom(UserCreationForm):
    first_name = forms.CharField(min_length=1, max_length=5)
    last_name = forms.CharField(required=False)
    # mbti = forms.CharField(min_length=4, max_length=4)

    class Meta:
        model = User
        fields = ('username', 'mbti', 'first_name', 'last_name',)