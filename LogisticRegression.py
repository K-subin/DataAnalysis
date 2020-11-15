# Logistic Regression

import torch

x_train = torch.FloatTensor([[1],[2],[3],[4],[5],[2.5],[3.5],[0],[3.1],[2.7],[2.8],[2.9]])
y_train = torch.FloatTensor([[1],[1],[1],[0],[0],[0],[0],[1],[0],[1],[1],[1]])

W = torch.zeros(1,1)
b = torch.zeros(1,1)

lr = 1.0

for epoch in range(3001):
  W.requires_grad_(True)
  b.requires_grad_(True)

  hypothesis = torch.sigmoid(torch.mm(x_train, W) + b)
  cost = torch.mean(
      -y_train * torch.log(hypothesis)
      -(1 - y_train) * torch.log(1 - hypothesis)
  )

  cost.backward()
  with torch.no_grad() as grd:
    W = W - lr * W.grad
    b = b - lr * b.grad

    if epoch % 100 == 0:
      print('epoch: {}, cost: {:.6f}, W: {:.6f}, b: {:.6f}'.format(epoch, cost.item(), W.item(), b.item()))