# 머신러닝 순서

1. 데이터셋 불러오기

2. Train/Test set으로 데이터 나누기
```
sklearn.model_selection.train_test_split(X, Y, test_size)
````

3. 모델 객체 생성하기

4. 모델 학습 시키기
```
model.fit(train_X, train_Y)
```

5. 모델로 새로운 데이터 예측하기
```
predict on test data
```

