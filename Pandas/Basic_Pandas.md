# Pandas

## pandas?

- 데이터 처리와 분석을 위한 라이브러리
- 행과 열로 이루어진 데이터 객체를 만들고 다룰수 있음
- 대용량의 데이터들을 처리하는데 매우 편리

## pandas의 자료구조
- Series: 1차원
- DataFrame: 2차원
- Panel: 3차원

## pandas import하기
- pandas는 보통 numpy와 함께 import한다
```
import numpy as np 
import pandas as pd
```

### 불러온 data의 경로 설정법

- 상대경로 설정법
```
(csv자료형일때)
___ = pd.read_csv('파일경로')
```

- 절대경로 설정법
```
___ = pd.read_csv('파일의 절대경로')
```

### DataFile의 형태보기
```
___.shape
```

### DataFile의 정보보기
```
___.info()
```

### DateFile 정보요약
```
___.describe()
```

### DateFile에서 상위 n개의 데이터만 추출
```
___.head(n)
```

---

## 단일 요소 추출

- postion_based_indexing(행 번호를 기준으로 행 데이터 읽기)
    - iloc함수
``` ___.iloc[읽기 원하는 행 데이터 값]```

- Label_based_indexing(인덱스 기준으로 행 데이터 읽기)
    - loc함수
```___.loc[인덱스값, '컬럼값']```

---

numpy axis 축의 개념을 살펴보기

numpy의 전치행렬, 행렬곱(내적)

iloc와 loc를 숙지