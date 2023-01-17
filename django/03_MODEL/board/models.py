from django.db import models
# table 만드는곳
# Create your models here.
class Article(models.Model):
    # id 는 함수이기 때문에 자동으로 만들어짐

    # 짧은 str => CharField(길이제한 숫자)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    # 긴 str => TextField
    content = models.TextField()
    

    # 1. models.py 작성 및 수정
    # 2. python manage.py makemigrations <app_name> => models.py의 요청값에 대한 1차 시안만들기
    # 3. python manage.py migrate <app_name> => db테이블 만들기
    # 4. python manage.py shell 
    # 5. 쉘에서 나올땐 ctrl + d 

    # CRUD 오퍼레이션 -> DB가 할 수 있는 행위 (만들고, 읽고, 수정하고, 삭제)