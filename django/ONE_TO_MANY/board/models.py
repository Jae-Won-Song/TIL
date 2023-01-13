from django.db import models
from django.conf import settings
# Create your models here.



class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creates_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    # foreign key 사용시 필드명에 _id 붙이지 않기
    # migrate 하면 알아서 뒤에 _id 붙음
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    creates_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)