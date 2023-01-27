# 데이터 구조

데이터에 효율적인 접근 및 수정을 가능하게 하는 데이터의 구성, 관리, 저장형식을 의미한다

---

## 데이터의 분류

- 순서가 있는 데이터 구조(Orderd)
  - 문자열
  - 리스트
  - 튜플
- 순서가 없는 데이터 구조(Unorderd)
  - 셋(Set)
  - 딕셔너리(Dictionary)

---

### 문자열

```
.find(x)
``` 
- index값(위치) 찾는 메서드
- x의 첫번째 위치를 반환한다.
- 만약 리스트 내에 x 가 없으면 **-1을 반환한다.**

```
.index(x)
```

- x의 첫번째 위치를 반환한다.
- 만약 리스트 내에 x 가 없으면 **오류가 발생한다**.

```
.startswith(x), /.endswith(x)
```
- .startswith(x) : 문자열이 x로 시작하면 True를 반환하고 아니면 False를 반환합니다.
- .endswith(x) : 문자열이 x로 끝나면 True를 반환하고 아니면 False를 반환합니다.

---

### 기타 문자열 관련 검증 메서드

- .isalpha() : 문자열이 (숫자가 아닌)글자로 이루어져 있는가?
- .isspace() : 문자열이 공백으로 이루어져 있는가?
- .isupper() : 문자열이 대문자로 이루어져 있는가?
- .istitle() : 문자열이 타이틀 형식으로 이루어져 있는가?
- .islower() : 문자열이 소문자로 이루어져 있는가?

---

### 숫자 판별 메서드

- .isdecimal(): 문자열이 0~9까지의 수로 이루어져 있는가?
- .isdigit(): 문자열이 숫자로 이루어져 있는가?
- .isnumeric(): 문자열을 수로 볼 수 있는가?

---

### 문자열 변경

## ★★
```
.replace(old, new[, count])
```
- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환합니다.

- count를 지정하면 해당 갯수만큼만 시행합니다.
---
## ★

```
.strip([chars])
```

- 특정한 문자들을 지정하면 
  - 양쪽을 제거하거나(strip) 
  - 왼쪽을 제거하거나(lstrip)
  - 오른쪽을 제거합니다(rstrip).

- chars 파라미터를 지정하지 않으면 공백을 제거합니다.
- chars 파라미터를 지정하면 모든 조합을 이용하여 제거합니다.
---

```
.split([chars])
```

- 문자열을 특정한 단위로 나누어 리스트로 반환합니다.

---
```
'separator'.join(iterable)
```

- iterable 의 문자열들을 separator(구분자)로 이어 붙인(join( )) 문자열을 반환합니다.

- 다른 메서드들과 달리, ***구분자가*** join 메서드를 제공하는 문자열입니다.
---
```
.capitalize()
.title()
.upper()

```
- __.capitalize() : 앞글자를 대문자로 만들어 반환합니다.

- __.title() : 어포스트로피(')나 공백 이후를 대문자로 만들어 반환합니다.

- __.upper() : 모두 대문자로 만들어 반환합니다
---
```
.lower() 
.swapcase()
```
- __.lower( ) : 모두 소문자로 만들어 반환합니다.

- __ .swapcase( ) : 대 <-> 소문자로 변경하여 반환합니다.

---

## List

- 변경 가능하고(mutable)

- 순서가 있고(ordered) 

- 순회 가능함(iterable)

---

```
.append(x)
```
리스트에 값을 추가할 수 있습니다.

- a[len(a):] = [x] 와 동일합니다.

---

```
.extend(iterable)
```
리스트에 iterable(list, range, tuple, string) 값을 붙일 수 있습니다.
- a[len(a):] = **iterable** 와 동일합니다.

---

```
.insert(i, x)
```
정해진 위치 i에 값을 추가합니다.

---

```
.remove(x)
```
리스트에서 **값**이 x인 첫번째 항목을 삭제합니다.

삭제할 항목이 없다면 error이 발생합니다.

---
## ★★
```
.pop([i])  
```
- 삭제되는 값을 return
- 정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환(삭제한 값이 출력)합니다.
- i가 지정되지 않으면 마지막 항목을 삭제하고 되돌려줍니다.

---

```
.clear()
```
- 리스트의 모든 항목을 삭제합니다.

---

## 탐색 및 정렬

```
.index(x)
```
- x 값을 찾아 해당 index 값을 반환합니다.

---

```
.count(x)
```
- 원하는 값의 개수를 반환합니다.

---

```
.sort()
```
- 리스트를 정렬합니다.

- 내장함수 sorted() 와는 다르게 원본 list를 변형시키고, **None**을 리턴합니다.

- 파라미터로는 key와 reverse가 있습니다.

---

```
.reverse()
```
- 리스트의 element들을 제자리에서 반대로 뒤집습니다. 정렬하는 것이 아닌 원본 순서를 뒤집고 수정합니다.

- 내장함수 reversed() 와는 다르게 원본 list를 변형시키고, **None**을 리턴합니다.

- sort와 마찬가지로, 파라미터 key와 reverse가 있습니다.

---

## 튜플(tuple)

- 변경할 수 없는 불변(Immutable) 자료형
- 값을 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만을 지원합니다.

```
.index(x[, start[, end]])
```

- 튜플에 있는 항목 중 값이 x 와 같은 첫 번째 인덱스를 돌려줍니다.

```
.count(x)
```
- 튜플에서 x 가 등장하는 횟수를 돌려줍니다.


---

## 셋(Set)

- 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)

```
.add(elem)
```
- elem을 셋(set)에 추가합니다.

```
.discard(elem)
```
- elem을 셋(set)에서 삭제합니다.

- remove와 다른 점은 elem이 셋(set) 내에 존재하지 않아도, 에러가 발생하지 않는다
```
.remove(elem)
```
- elem을 셋(set)에서 삭제하고, 셋(set) 내에 elem이 존재하지 않으면 KeyError가 발생
- ---

## 딕셔너리(Dictionary)

- 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)
  - Key: Value 페어(pair)의 자료구조


```
.get(key[, default])
```
- key를 통해 value를 가져옵니다.
  - key가 존재하지 않을 경우 None을 반환합니다. **KeyError가 발생하지 않습니다.**

---
```
.setdefault(key[, default])
```
- dict.get() 메서드와 비슷한 동작을 하는 메서드로, key가 딕셔너리에 있으면 value를 돌려줍니다.

- *get과 다른 점*은 key가 딕셔너리에 없을 경우, default 값을 갖는 key 를 삽입한 후 default 를 반환한다는 점입니다. 만일 default가 주어지지 않을 경우, None 을 돌려줍니다.

---

## 추가 및 삭제

```
.pop(key[, default])
```
- key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환합니다.
  - default가 없는 상태에서 해당 key가 딕셔너리에 경우, KeyError가 발생합니다.

---

```
.update([other])
```
- other 가 제공하는 key,value 쌍으로 딕셔너리를 덮어씁니다. 
    - other 는 다른 딕셔너리나 key/value 쌍으로 되어있는 모든 iterable을 사용 가능

---

