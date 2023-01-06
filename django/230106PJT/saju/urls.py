# URL
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'saju'

urlpatterns = [
    path('', views.user_input, name = 'saju'),
    
]

