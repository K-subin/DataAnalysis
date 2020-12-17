import sys, re, math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# === Task2. matplotlib을 활용하여 각 단어의 출현 횟수 순위(x축)와 각 단어의 출현 횟수 (y축)를 log scale에서 출력하고, 지프의 법칙을 따르는지 확인하기 ===

freq=[]
for line in sys.stdin:
    freq.append(int([x for x in re.split('[\t\n]+', line)][1]))
rank = [x for x in range(1, len(freq) + 1)]

#======== log scale 그래프 그리기
plt.xscale('log')
plt.yscale('log')

plt.xlabel('rank')
plt.ylabel('frequency')
plt.title('Zipf plot')

plt.plot(rank, freq, 'r-')

plt.savefig('plot.png')

#========= 선형회귀를 이용하여 s, c 구하기
# freq = c * (rank ^ -s) --> y = freq, x = rank --> y = c * (x ^ -s)
# log(y) = log(c) - s * log(x) --> Y = A + BX 꼴의 선형회귀이다.

linear_regression = LinearRegression()
log_freq = np.array(list(map(math.log10, freq)))
log_rank = np.reshape(list(map(math.log10, rank)), (-1, 1))
linear_regression.fit(X=log_rank, y=log_freq)
print('c =', 10 ** linear_regression.intercept_)
print('s =', -(linear_regression.coef_)[0])