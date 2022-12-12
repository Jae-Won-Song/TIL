# git의 기초
### git 사용을 위해선 사용자 서명이 필요함
- 사용자 서명을 위한 명령어

 
  > git config --global user.name "____"  →  github에 등록할 자신의 서명

  > git config --global user.email "email" →  github에 등록할 자신의 email주소
  


## git의 개념과 학습 이유

- git이란?
 >버전 관리 프로그램 

 - 학습이유?
  >오픈소스 프로그램이기 때문에 접근이 쉽다

  >github에 여러가지 소스코드들이 매우 많아 개발에 용이함

  >버전관리에 매우 용이함


### VCS 

- 버전 관리 시스템 ``version control system``
  - 프로젝트가 꼬였을경우 복구를 돕기 위함
  - 소스 코드의 변경사항을 추적하기 위함
  - 많은 오픈 소스 프로젝트에서 버전관리는 필수


### Working Directory

- 현재 작업중인 디렉토리
---
### Stage
- commit을 하기전 git파일버전을 1차적으로 저장함
- 이 상태에서 파일이 지워지면 마지막으로 commit한 부분에서 불러옴

### Commit
- 최종적 파일버전 저장 
- rm명령어로 파일이 지워졌어도 이 시점부터 복원 가능

---
## **git 명령어**

|명령어|설명|예시|
|-|-|-|
|```git init```|폴더를 git폴더로 만든다|git init __|
|```git add __```|git파일을 스테이징시킨다|git add __|
|```git add .```| 현재 디렉터리에 있는 모든파일을 스테이징한다|git add .|
|```git commit -m __```|git파일을 저장(촬영)한다|git commit -m __|
|```git status```|git파일들 상태를  보여준다|git status|
|```git log```|git 파일들의 변경사항을 보여준다|git log|
|```q```|git log 상태에서 빠져나온다|q|

---

