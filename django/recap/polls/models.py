from django.db import models
from  django.conf import settings
# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    # 알아서 db컬럼은 user_id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Reply(models.Model):
    content = models.CharField(max_length=200)
    # reply.____.all() => 이 reply 와 M:N 관계를 가지고 있는 User들이 나와야한다
    vote_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
    # user.____.all()=> 이 User와 M:N Reply가 나와야한다.
     related_name='vote_replies')
    # db 컬럼은 user_id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # db 컬럼은 question_id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def is_voted(self, user): # reply.is_voted(user)
        return self.vote_users.filter(pk=user.pk).exists()
