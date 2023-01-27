from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# u1.stars.add(u2)  => u1이 u2를 팔로우
# u2.stars.add(u1)  => u2가 u1을 팔로우
# u1.fans.remove(u2) => u2가 u1을 언팔

class User(AbstractUser):
    fans = models.ManyToManyField('self', symmetrical=False, related_name='stars')
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
    