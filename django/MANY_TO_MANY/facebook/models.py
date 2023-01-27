from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    
    def __str__(self):
        return f'{self.pk}:{self.name}'

class Feed(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='feeds')
    content = models.TextField()
    like_people = models.ManyToManyField(Person, related_name='like_feeds')
    
    



class Comment(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)


    '''
p1 = Person.objects.create(name='neo', age='23')
p2 = Person.objects.create(name='justin', age=25)
p3 = Person.objects.create(name='alex', age=23)

f1 = Feed.objects.create(content='콧물이난다..', author=p1)
c1 = Comment.objects.create(content='훌쩍..', feed=f1, author=p2)
    

    [related_name]
p1. like_feeds  .all() # 좋아요 한 게시글 모두

    [field_name]
f1. like_people .all() # 좋아요 한 사람들 모두


p1.like_feeds.add(f1)  # p1이 좋아요 한 게시글에 f1 추가 => join테이블에 p1 f1레코드 추가
f1.like_people.add(p1) # 결과 같음 (데이터 중복 안됨)

p1.like.feeds.remove(f1) # join테이블에서 p1, f1으로 구성된 레코드 삭제
f1.like_people.remove(p1) # 결과 같음


    '''