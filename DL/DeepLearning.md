# DeepLearuning?

- 딥뉴럴네트워크(DNN)를 활용하여 학습하는 머신러닝 알고리즘 (Deep = Hidden layer가 2개 이상)

## 전통적인 머신러닝과 딥러닝의 차이

- 전통적인 머신러닝
- 사람이 직접 데이터의 중요한 부분들을 찾아 Feature로 정해주어야 함
  - Input -> Feature Engineering & Feature Selection -> Features -> Regressor of Classifier

<br>

- 딥러닝
- 신경망 내부에서 자체적으로 데이터의 중요한 Feature를 찾거나 구성함
  - Input -> Feature Extraction -> Regressor or Classfier -> Output

---

# 단층 퍼셉트론

- 뉴런을 본따 만든 알고리즘 하나의 단위
- 2가지 연산을 적용하여 출력값 계산
  1.  넘겨져 온 데이터와 세터들의 Linear combination +
      1. 이전 Layer혹은 외부로부터 넘겨져 온 데이터와 각 세터 사이의 Linear Combination
  2.  Activation fuction
      - 이전 레이어의 모든 입력에 대한 가중 합을 받아 `출력값을 생성`하여 `다음 레이어로 전달` 하는 `비선형 함수`
        - 넘겨져 온 데이터와 세터들의 Linear combination 을 계산
        - 선형결합의 결과에 Activation function(활성화 함수)을 적용
          - 대표적 Activation function
            1. Sigmoid
            2. tanh
            3. ReLU
            4. Leaky ReLU
            5. ELU
            6. Step
  3.  선형결합들로만 반복해서 Layer를 쌓는다면 선형회귀분석

# 다층 퍼셉트론

- 복수의 Perceptron을 연결한 구조

# 인공신경망 (Neural Network)

- Perceptron을 모은 Layer를 깊이 방향으로 쌓아나가면서 복잡한 모델을 만들어내어 보다 더 어려운 문제를 풀어낼 수 있음

- Input Layer
  - 외부로부터 데이터를 입력받는 신경망 입구의 layer
- Hidden layers == Learnable kernels
  - Input layer 와 Output layer 사이의 모든 layers
- Output Layer
  - 모델의 최종 연산 결과를 내보내는 신경망 출구의 layer

# 오차 역전파 알고리즘

=> 신경망의 효율적인 학습방법

- 학습된 출력 값과 실제값과의 차이인 오차를 계산하여 Feedforward 반대인 역방향으로 전파 하는 알고리즘

```
모델이 틀린 정도를 역방향으로 전달하며
미분하고 곱하고 더하는 것을 반복하여
parameter(세터)를 갱신한다
```

---

## Nerual Network Optimization

### Gradient descent 를 활용한 신경망의 학습과정

1. 모든 Parameter 세터를 초기화하고
2. Cost Function상의 가장 낮은 지점을 향해 나아가며
3. 선택한 Gradient descent method 를 적용해 세터를 계속 update

---

### Nerual Network Optimization

1. Weight Initialization
   - Gradient descent를 적용하기 위한 첫 단계는 모든 Parameter 세터를 초기화하는것
   - 초기화 시점의 **작은 차이가 학습의 결과를 뒤바꿀 수 있으므로** 보다 나은 초기화 방식을 모색하게 됨
     1. Use Xavier Initialization
        - 활성화 함수로 Sigmoid 함수나 tanh함수를 사용할 때 적용
        - 다수의 딥 러닝 라이브러리들에 Default로 적용
        - 표준편차가 루트1/n인 정규븐포를 따르도록 가중치 초기화
          - n = # of nodes of previous layer
     2. He Initialization
        - 활성화 함수가 ReLu함수일 때 적용
        - 표춘편차가 루트2/n인 정규분포를 따르도록 가중치 초기화
