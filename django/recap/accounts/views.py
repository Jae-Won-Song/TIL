from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationFrom


User = get_user_model()

HOME_URL = 'polls:question_index'

@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return HttpResponseBadRequest('이미 가입 되었습니다.')

    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(HOME_URL)
    else:
        form = CustomUserCreationFrom()

    context = {'form':form,}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    # login 한 사용자라면
    if request.user.is_authenticated:
        return HttpResponseBadRequest('이미 로그인 하였습니다.')

    if request.method == 'POST':
        # 많은 form중에 얘만 1번 인자 request
        form = AuthenticationForm(request, request.POST)
        # 사용자가 입력한 username / password 가 맞다면,
        if form.is_valid():
            # AuthenticationForm => User create가 아니기때문에 다른 메서드 제공
            user = form.get_user()
            # 로그인 시키기(쿠키 세팅) 
            auth_login(request, user)
            return redirect(HOME_URL)
    else:
        form = AuthenticationForm()
    context = {'form':form,}
    return render(request, 'accounts/login.html', context)



def logout(request):
    auth_logout(request)
    return redirect(HOME_URL)

# which follower manage place -> Profile Page
# /accounts/aro
@require_safe
def profile(request, username):
    me = request.user
    profile_user = get_object_or_404(User, username=username)
    if me.is_authenticated:
        is_following = me.stars.filter(pk=profile_user.pk).exists()
    else:
        is_following = None
        
    context = {
        'profile_user' : profile_user,
        'is_following' : is_following,
    }
    
    return render(request, 'accounts/profile.html', context)
    
# 실제 팔로우 기능
# /accounts/aro/follow/
@require_POST
def follow(request, username):
    me = request.user
    you = get_object_or_404(User, username=username)
    if me == you:
        return HttpResponseBadRequest('나르시즘..')

    is_following = me.stars.filter(pk=you.pk).exists()
    # 내가 나를 팔로우 불가능
    if is_following:
        me.stars.remove(you)
    else:
        me.stars.add(you)
    return redirect('accounts:profile', you.username)

    # 요청 보낸 사용자 / 대상 사용자
 