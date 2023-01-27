# venv (가상환경)

1. 프로젝트 파일을 만든뒤
2. soruce.venv.scripts/activate명령어를 통해
3.  global python에서 venv폴더로 타겟을 바꿔줌


---
## 가상환경 생성과정
1. mkdir 프로젝트폴더이름
2. ``` python -m venv venv ```  독립 환경 생성
3. touch .gitignore  **https://gitignore.io** 에서 "python" "django" "venv" 입력하고 내용 복사
4. touch README.md 파일 생성
---
## Windows 환경에서 venv 활성화
- source venv/Scripts/activate
- venv가 잘 실행됐다면 터미널 유저 이름에 venv가 나타남.


## 추가 설치한 패키지들이 있다면
- pip freeze > requirements.txt


프로젝트의 시작
```
앱만들기 
앱안에 템플릿 만들고
앱애서 urls만들고
마스터폴더에서 templates랑 베이스html만들고
세팅에서 템플릿,인스톨앱에 등록
```