# oop
- 객체(Object)
- 객체지향프로그래밍 (Object Oriented Programming)
- 클래스와(Class) 객체 (Object)

## 객체
 파이썬에서 **모든것은 객체**이다

 모든 객체는 **타입, 속성, 조작법**(method을 가진다

### 클래스(Class)
- 클래스는 공통된 속성(attroibute)과 조작법(method을 가진 객체들의 분류

### 인스턴스 (Instance)
- 특정 클래스의 실제 데이터 예시
- 파이썬에서 모든것은 객체이고, 모든객체는 특정 클래스의 연속이다

- 인스턴스 생성
  - 인스턴스 = 클래스( )

---

```
일반 변수/함수명은 전부 소문자에, 띄어쓰기가 필요하면_로 => snake case

클래스명은 첫글자 대문자에, 띄어쓰기 필요하면 또 대문자로 => PascalCase(UpperCamelCase)
```

## 속성(attribute)과 메서드(method)


- 속성(attribute)은 객체의 상태, 데이터를 뜻함
- 활용법 <객체>.<속성>
---
- 메서드(method)
- 특정 객체가 할 수 있는 행위를 뜻함
- 활용법 <객체>.<메서드>( )

## 생성자(constructor) 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 함수
---

## 매직(스페셜)메서드

- 더블언더바가 있는 메서드

```
__something__
```
- ex
```
__str__(self)',
'__len__(self)',
'__repr__(self)',
'__lt__(self, other)',
'__le__(self, other)',
'__eq__(self, other)', => ==
'__ne__(self, other)', 
'__gt__(self, other)', => >
'__ge__(self, other) 
```

## 클래스 변수

- 클래스의 속성
- 모든 인스턴스가  공유
- 클래스 선언 내부에서 정의
- **클래스.변수명**으로 접근 및 할당

ex)
```
class Circle:
    pi = 3.14

print(Circle.pi)
```

## 클래스메서드

- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용
- **메서드 호출시, 첫번째 인자로 클래스 cls가 전달됨**
---
★ **변수는 LEGB순으로 찾고 **

★ 객**체의 상태나 메서드는 instance => class => 상위class..순으로 찾는다**

---

# OOP의 핵심개념

- 추상화
- 상속
- 다형성
- 캡슐화

## 추상화 (Abstraction)
- 세부적인 내용은 감추고 필수적인 부분만 표현
- 현실 세계를 설계에 반영하기 위해 사용
- 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출해 기본클래스로 작성하여 활용
  
## 상속

- 클래스에서 가장 큰 특징은 상속
- 코드 재사용성이 높음

모든 클래스는 **type클래스**를 **상속**받았기 때문에 dir에서 실제 내가 정의하지 않아도 여러가지 많이 나온다.

## 다형성
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음
- 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 각기 다른 방식으로 응답될 수 있음


## 캡슐화
- 객체의 일부 구현내용에 대해 외부로부터의 직접적인 액세스를 차단
- 파이썬에서의 캡슐화는 **암묵적**으로 존재하지만 언어적으로는 존재하지않는다.

- **언더바 1개**로 시작하는 메서드나 속성들이 해당

