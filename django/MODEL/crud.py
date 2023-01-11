from board.models import Article

#  아티클 생성 전
# python manage.py makemigrations,
# python manege.py makemigrate 으로 테이블 생성!




# Create 

## 1
article = Article()
article.title = '첫번째 글'
article.content = '와 내가 처음이야'
article.author = '송재원'
article.save()

## 2
article = Article(title='2번글', content='뭐지', author='유아인')
article.save()

## 3
Article.objects.create(title='3번글', content='몰라', author='현빈')
# objects => 아티클의 매니저


# Read, Retrieve (조회)
article = Article.objects.get(id=1)  # => 1번에 저장 / id = pk(primary key) 서로 같은 개념
article.id  # => id조회 (pk)
article.title   # => title조회
article.content   # => content조회
article.author   # => author조회

## 전체조회
Article.objects.all()  # => 모든 게시물을 다 뽑아옴
articles = Article.objects.all()  #  => 변수 저장
for article in articles:
    print(article.title)
    # 아티클의 제목 출력

# Update (수정)
article = Article.objects.get(id=3)  #  먼저 수정할 게시글을 고른다.
article.title = '수정한 글'
article.content = '바뀌어라 얍'
article.save()

# Delete / Destroy (삭제)
article = Article.objects.get(id=3)  # 먼저 삭제할 게시글을 고른다.
article.delete()

