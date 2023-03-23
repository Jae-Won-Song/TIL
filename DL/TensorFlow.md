 # TensorFlow?

 - numpy의 상위호환
 - GPU 활용 가능
 - python API 제공 / 실행되는 환경은 C/C++

### Tensorflow 1.0~
- 밑바닥부터 인공신경망을 쌓아서 올라감

### Tensorflow 2.0~
- Keras 기반 1.0보다 간결한 코드구조

### 장점

- python문법이 메인
  - 다른 여러 언어에서도 사용 가능
- 확장성↑ (여러기기에서 사용가능)

## Basic TensorFlow
1. Building a TensorFlow Graph(선언)
- Tensor 들 사이의 연산 관계를 계산그래프로 `정의 & 선언`
2. Executing the TensorFlow Graph(실행)
- 계산 그래프에 정의된 연산을 tf.Session을통해 실제로 `실행`

