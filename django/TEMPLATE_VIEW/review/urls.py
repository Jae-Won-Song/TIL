from django.urls import path
from . import views

# 변수명 반드시 app_name 
app_name = 'review'
# URL 구성 맨 앞에 'review/'는 master url 에서 검사가 끝남
urlpatterns = [
    # 패턴 '(review/)'index/ 가 요청으로 들어온다면, views.py에 정의된 함수실행
    path('', views.index, name='index'),
    # review/hello/
    path('hello/', views.hello, name='hello'),
]


# review/hello/ => view hello 함수실행 => hello.html을 응답(렌더)
