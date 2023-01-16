from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    MBTI_CHOICES = [
        ('INTJ', 'INTJ'),
        ('INTP', 'INTP'),
        ('ISTP', 'ISTP'),
        ('ISFP', 'ISFP'),
        ('ENTJ', 'ENTJ'),
        ('ENTP', 'ENTP'),
        ('INFJ', 'INFJ'),
        ('INFP', 'INFP'),
        ('ENFJ', 'ENFJ'),
        ('ENFP', 'ENFP'),
        ('ISTJ', 'ISTJ'),
        ('ISFJ', 'ISFJ'),
        ('ESTJ', 'ESTJ'),
        ('ESTP', 'ESTP'),
        ('ESFP', 'ESFP'),    
    ]
    mbti = models.CharField(max_length=4, choices=MBTI_CHOICES)
    