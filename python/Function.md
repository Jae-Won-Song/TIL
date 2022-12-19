# 함수

- input(x) 값에 따라서 output f(x)값이 계속 달라짐.
- 특정한 기능(function)을 하는 코드의 묶음

## 함수의 사용 이유

- 가독성
- 재사용성
- 유지보수


함수의 선언과 호출

- 함수의 선언은 def 키워드를 활용
- 들여쓰기(4spaces)로 함수의 body(코드 블록)를     
작성
    - Docstring은 함수 body 앞에 선택적으로 작성 가능
- 함수는 매개변수(parameter)를 넘겨줄 수도 있다
- 함수는 동작후에 return을 통해 결과값을 전달한다
- 반드시 하나의 객체를 반환한다 (return 값이 없으면, None을 반환)
- 함수는 호출은 함수명()으로 한다
예) func() / func(val1, val2)


## 함수 구하는 공식

```
def <함수이름>(parameter1, parameter2):
    <코드 블럭>
    return value

```
- ex)
  -  선언부 (input 관리) => 선언시 input 값은 매개변수 (parameter)
def ___(n):
    
  - 로직(알고리즘)주요기능
    result = n ** 3
    
  - 최종 return 결과
    return(input) result(output)

## 함수의 Output

### 함수의 return
- 오직 한 개의 객체(값)만 반환된다
- 함수가 return되거나 종료되면 함수를 호출한 곳으로 돌아간다
  - 객채값을 정의하고  함수를 할당한다

## 함수의  Input

```
def func(x):
      return x + 2 
```

x는 매개변수(parameter)

입력을 받아 함수 내부에서 활용

**함수를 정의하는 부분에서 확인 가능**

---

### 기본 인자값

