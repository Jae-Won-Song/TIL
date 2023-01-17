from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

# User를 커스텀 하면(accounts.User) 반드시 회원가입 Form도 직접 만들어야함.
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields=('username', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')