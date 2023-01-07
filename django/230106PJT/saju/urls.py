# URL
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'saju'

urlpatterns = [
    path('user_input/', views.user_input, name = 'saju'),
    path('user_output/', views.user_output, name = 'saju'),
    
]

