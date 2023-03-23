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
  1.  넘겨져 온 데이터와 $\theta$들의 Linear combination +
      1. 이전 Layer혹은 외부로부터 넘겨져 온 데이터와 각 $\theta$ 사이의 Linear Combination
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

1. 모든 Parameter $\theta$를 초기화하고
2. Cost Function상의 가장 낮은 지점을 향해 나아가며
3. 선택한 Gradient descent method 를 적용해 $\theta$를 계속 update

---

### Nerual Network Optimization

1. Weight Initialization
   - Gradient descent를 적용하기 위한 첫 단계는 모든 Parameter $\theta$를 초기화하는것
   - 초기화 시점의 **작은 차이가 학습의 결과를 뒤바꿀 수 있으므로** 보다 나은 초기화 방식을 모색하게 됨
     1. Use `Xavier Initialization`
        - 활성화 함수로 Sigmoid 함수나 tanh함수를 사용할 때 적용
        - 다수의 딥 러닝 라이브러리들에 Default로 적용
        - 표준편차가 루트1/n인 정규븐포를 따르도록 가중치 초기화
          - n = # of nodes of previous layer
     2. `He Initialization`
        - 활성화 함수가 ReLu함수일 때 적용
        - 표춘편차가 루트2/n인 정규분포를 따르도록 가중치 초기화


---
<!-- 23.03.23 -->

2. Weight regularization
- 기존의 Gradient Descent 계산 시 y축에 위치해 있던 Cost function은 Training data에 대해 모델이 발생시키는 Error값의 지표
- Training data만 고려된 이러한 Cost Function을 기준으로 하여 Gradient Descent를 적용하면 Overfitting에 빠질 수 있음
- 모델이 복잡해질수록 모델 속에 숨어있는 $\theta$들은 그 개수가 많아지고 절대값이 커지는 경향이 있음(숨겨진 $\theta$들이 값을 갖게 됨)
- 모델이 복잡해질수록 그 값이 커지는 `세터에 대한 함수를 기존의 Cost function에 더하여` Trade-off관계 속에서 최적값을 찾을 수 있음

## Regularization Term

### L1 정규화
- Lasso
- 가중치의 `절대값의 합에 비례`하여 가중치에 페널티를 줌
- 관련성이 없거나 매우 낮은 특성의 가중치를 정확히 0으로 유도, 모델에서 해당 특성을 배제하는 데 도움이 됨 (Feature selection 효과)
### L2 정규화
- Ridge
- 가중치의 `제곱의 합에 비례`하여 가중치에 페널티를 준다
- 큰 값을 가진 가중치를 더욱 제약하는 효과
- 가장 `많이 사용`되는 정규화
  
```
L1 & L2 Regularization = Weight Decay(가중치 감퇴/감소)
```

### Regularization Rate
- 정규화율($\lambda$)
- 스칼라 값
- 정규화 함수의 상대적 중요도를 지정
- 정규화율을 높으민 과적합이 감소하지만 모델의 정확성이 떨어질 수 있음 (Underfitting)
- $\theta$의 수가 아주 많은 신경망은 정규화율을 아주 작게 주기도 함

---
### Stochastic Gradient Descent(확률적 경사 하강법)

**하나의 Training data 마다 Cost를  계산하고 바로 Gradient descent를 적용해 weight를 빠르게 update**
- 한개의 Training data마다 매번 weight를 갱신하기 때문에 신경망의 성능이 들쑥날쑥 변함 (Cost값이 안정적으로 줄어들지 않음)
- 최적의 Learning rate를 구하기 위해 일일이 튜닝하고 수렴조건(early-stop)을 조정해야함

### Mini-Batch Stochastic Gradient Descent
**Training data에서 일정한 크기 == Batch size 의 데이터를 선택하여 Cost function 계산 및 Gradient descent적용**
- 앞선 두 가지 Gradient descent기법의 단점을 보완하고 장점을 취함
- 설계자의 의도에 따라 속도와 안정성을 동시에 관리할 수 있으며 GPU 기반의 효율적인 병렬 연산이 가능해진다

#### 1 epoch
- 전체 데이터를 한번에 다 넣는것 

#### Batch size
- 1epoch를 n토막으로 나눈것

