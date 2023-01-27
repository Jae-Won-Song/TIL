# accouts/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required

# 수업으론 다루지 않음
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('board:article_index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        # 다른 form 과 인자가 구성이 다름
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            # None / URL string
            next = request.GET.get('next')
            return redirect(next or 'board:article_index')
                
    else:
        form = AuthenticationForm()
    context = { 'form': form, }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('board:article_index')


# 아래는 수업에서 다루지 않음
@login_required
def profile(request, username):
    profile_user = get_object_or_404(User, username=username)  # User 모델에서 username으로 검색하여 찾은 객체
    
    context = {
        'profile_user': profile_user,
    }

    return render(request, 'accounts/profile.html', context)
    

# 회원정보 변경/삭제 (이런게 있구나..)
@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile', user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/update.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('board:article_index')


@login_required
@require_http_methods(['GET', 'POST'])
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # PasswordChangeForm 은 forms.Form을 상속받았으나, 예외적으로 save 메서드가 존재
            user = form.save()

            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, request.user)
            
            return redirect('accounts:profile', user.username)
    else:    
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/password.html', context)
