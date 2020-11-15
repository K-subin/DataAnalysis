# optimizer 사용해보기

import torch
import matplotlib.pyplot as plt

x_train = torch.FloatTensor([[1],[2],[3],[4],[5],[2.5],[3.5],[0],[3.1],[2.7],[2.8],[2.9]])
y_train = torch.FloatTensor([[1],[1],[1],[0],[0],[0],[0],[1],[0],[1],[1],[1]])

W = torch.zeros(1,1)
b = torch.zeros(1,1)

for epoch in range(3001):
    W.requires_grad_(True)
    b.requires_grad_(True)

    hypothesis = torch.sigmoid(torch.mm(x_train, W) + b)
    cost = torch.mean(
        -y_train * torch.log(hypothesis)
        -(1 - y_train) * torch.log(1 - hypothesis)
    )
    optimizer = torch.optim.SGD([W,b], lr=1.0)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print('epoch: {}, cost: {:.6f}, W: {:.6f}, b: {:.6f}'.format(epoch, cost.item(), W.item(), b.item()))


# Matplotlib으로 결과 시각화
W.requires_grad_(False)
b.requires_grad_(False)

plt.scatter(x_train, y_train, c="black", label="Training data")

X = torch.linspace(0,5,100).unsqueeze(1)
Y = torch.sigmoid(torch.mm(X,W)+b)
plt.plot(X,Y, c="#ff0000", label="Fitting line")
plt.legend()

plt.ylabel("Probability of 1 (Y)")
plt.xlabel("Input (X)")

plt.show()