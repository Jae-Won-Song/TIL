# git의 기초
### git 사용을 위해선 사용자 서명이 필요함
- 사용자 서명을 위한 명령어

 
  > git config --global user.name "____"  →  github에 등록할 자신의 서명

  > git config --global user.email "email" →  github에 등록할 자신의 email주소
 ---
  
  ## ※ WARNING
1. **현재 위치를 잘 확인한다.**
2. **Repo 안에서 repo (master)를 만들지 않는다. (Master 떠있으면 `git init` X)**
3. **Home(`~`)에서 init 하지 않는다.**
4. **(지금은) github에서 직접 수정하지 않는다.**
​
---

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
|```git add <스테이징시킬 디렉터리>```|git파일을 스테이징시킨다|git add __|
|```git add .```| 현재 디렉터리에 있는 모든파일을 스테이징한다|git add .|
|```git commit -m```|git파일을 저장(촬영)한다|git commit -m <파일명>|
|```git status```|git파일들 상태를  보여준다|git status|
|```git log```|git 파일들의 변경사항을 보여준다|git log|
|```git log--oneline```|git log를 압축하여 보여준다|git log --oneline|
|```cat ~/.gitconfig```|git에 등록되어있는 이메일과 서명을 본다|cat ~/.gitconfig|
|```q```|git log 상태에서 빠져나온다|q|
|```git remote add```|git hub에 원격저장소를 추가한다|git remote add <저장소이름> <URL.>|
|```git push```|git hub에 commit파일 등록|git push <저장소이름> <파일명>|
|```git pull```|git hub에 등록한 commit파일 불러오기|git pull <저장소이름> <파일명>|
|```git clone```|git을 처음 사용한 컴퓨터에 git hub파일 불러오기|git clone [REPO_URL] [DIR]|
|```git remote -v```|github의 원격저장소 목록을 확인한다|git remote -v|

---
## git hub commit 과정
```
1. git add .
   1. 수정, 생성한 git 파일을 스테이징한다.
2. git commit -m <파일이름>
   1. 스테이징 된 파일을 스냅샷한다. 
3. git push <저장소이름> <파일이름>
```
---

## git hub pull 과정
```
1. git pull <저장소이름> <파일명>
```

---

## git 브랜치

- 독립적으로 개발을 진행
- 개발진행중 생각과 다르게 진행될때, 브랜치를 삭제함으로써 기존의 개발환경으로 돌아갈 수 있음
- 다른 버전관리프로그램과 달리 git 은 HEAD라는 특수한 포인터가 존재
---
``` master 브랜치 (배포 브랜치)는 프로그램이 정상 작동할 때 최종적으로 merge한다.```

---
- 보유중인 브랜치 확인
```
git branch
```
- 브랜치 생성
```
git branch __
```

- git 브랜치 이동
```
git switch __
```

- 브랜치들을 합친다
```
git merge__
```
- git __를 브랜치하고 브랜치한 __로 바로 이동
```
git switch -c __
```
- Merge 끝난후 남은 브랜치 지우기
```
git branch -d __
```
- Merge 끝난후 남은 브랜치 강제로 지우기
```
git branch -D __
```


---
Merge의 세가지 경우
- FastFoward ( + commit X)
- Automatic Merge ( + commit O)
- CONFLICT => Manual Commit ( + commit O but 내가함)

---


- PUSH함 => 안됨 => - PULL함 => 별일 없음 => PUSH

- PUSH함 => 안됨 => PULL함 => @@ => 고침 => add/commit => PUSH
- PUSH함 => 잘됨 => 끝
