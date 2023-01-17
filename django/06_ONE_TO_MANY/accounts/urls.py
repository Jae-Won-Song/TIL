# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # accounts/signup/
    path('signup/', views.signup, name='signup'),
    # accounts/login/
    path('login/', views.login, name='login'),
    # accounts/logout/
    path('logout/', views.logout, name='logout'),

    #(아래는 다루지 않음)
    # accounts/profile/neo/
    path('profile/<str:username>/', views.profile, name='profile'),
    # 회원정보 변경/삭제 
    # accounts/update/
    path('update/', views.update, name='update'),
    # accounts/delete/
    path('delete/', views.delete, name='delete'),
    # accounts/password/
    path('password/', views.password, name='password'),
]
