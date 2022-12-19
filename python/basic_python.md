# Python

## Python?
---
## 식별자 (이름)

- 대소문자를 구별한다
- - 이름은 영문알파벳, 밑줄, 숫자로 구성된다
- 첫 글자에 숫자가 올 수 없다
- 길이에 제한이 없다
- 사용 할 수 없는 몇가지 예약어가 있다
  - False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

---

## Python int, str, float

- int (integer)
  - 정수 

- str (string)
  - 문자 
- float
  - 소수점이 있는 숫자

---
     
### Python 명령어

> 명령어를 입력하면 구문에 있는 텍스트가 출력됨
```
print('구문')
```
> print문을 한줄로 이어서 쓰면 오류가 나는데, 
> 
> 이때 세미콜론 ; 또는 \를 통해 줄을 바꿈으로써 해결이 가능하다

**``※세미콜론은 줄이 바뀌기 때문에 잘 사용안함``**

```
print('hello world welcome(\)(;)
my world')
```
>웹 브라우저를 실행
```
import webbrowser 

webbroswer.open('URL')
```
- 같은 도메인의 다른 검색결과를 깔끔하게 가져오고 싶을때
```
for x in ['']: 
[URL상 다른 부분]
```
---

## Jupyter

### Jupyter notebook 접근

```
Jyputer notebook
```
- 웹이 자동으로 열리지 않을경우 터미널 아래에있는 URL 접속

---

# 시퀀스 자료형

## List

- 리스트는 대괄호[]로 만들 수 있음,
- 리스트 안에있는 **항목 변경 가능**

리스트 접근 (인덱스 접근) (대괄호)
-  l __ = [1, 2, 3]
-  list[l] = [1, 2, 3]
   - l[1] = 100
   - list[l] -> [1, 100, 3]

---

## tuple

튜플은 **수정 불가능**하다 

  튜플은 ()로 묶어서 표현

---

 ## range

 숫자의 시퀀스를 나타내기 위함
 range 안에 뭐가 있는지 보고싶을때
 - range(n)
   - list(range(n))

- 기본형 0~ n-1의 값
  - range(n)

- 범위 지정 n부터 n-1의 값
  - range(n, n-1)
    - 숫자를 오름차순으로 만들기위해선 range값을 그룹화 후 sort명령어를 사용함
    - ex) ___ = random.choice(numbers)
    - __.sort() ->메소드
  
- 범위, 스텝지정
  - range(n, n-1 m)
  -list(range(n, n-1 m))
    - n의 숫자에서 n-1의 숫자까지 m의 스텝으로 range만듦
  
---

## set

- 순서가 없는 자료구조
  - 수학에서의 집합과 동일하게 처리
  - {}를 통해서 만듦, 순서가 없고 중복된 값이 없음
  - 빈 집합 set을 만들려면 *set()*을 사용한다.

### 활용법
- a - b 차집합
- a | b 합집합
- a & b 교집합
---

## dictonary

- 딕셔너리는 key와 value로 나뉘어짐
  - dict_a = {'key' : 'value'}

- 딕셔너리 value 바꾸기
  - __ [key값] = 'value'

- 딕셔너리 value 추가
  - __[ ]


  

