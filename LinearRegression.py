# Linear Regression
# y = w1*x1 + w2*x2 + b  --> w1, w2, b 값 찾기

import torch
import matplotlib.pyplot as plt

x_train = torch.FloatTensor([[1,2],[3,2],[3,7],[1,1],[1,0]])
y_train = torch.FloatTensor([[4],[8],[23],[1],[-2]])
print('x_train :\n', x_train)
print('y_train :\n', y_train)

# w, b 초기화
W = torch.zeros(2,1) # x의 독립변수가 2개 - 곱셈을 자연스럽게 하기 위해
b = torch.zeros(1,1) # y의 독립변수가 1개

# learning rate 설정
lr = 0.01

# 반복횟수 설정
for epoch in range(3001):
  W.requires_grad_(True)
  b.requires_grad_(True)

  # 가설함수, cost 설정
  hypothesis = torch.mm(x_train, W) + b
  cost = torch.mean((hypothesis - y_train) ** 2)

  # 기울기 계산 -> W, b 업데이트
  cost.backward()
  with torch.no_grad():  # 새로운 기울기 받기 위해
    W = W - lr * W.grad
    b = b - lr * b.grad
  
  if epoch % 300 == 0:
    print(f'epoch : {epoch}, cost : {cost.item():6f}, W : {W.squeeze()}, b : {b}')