import numpy as np
import matplotlib.pyplot as plt

# 1000개의 랜덤 데이터 생성하기
data = np.random.randint(low=155, high=195, size=1000)
print('평균 = {}, 표준편차 = {}'.format(np.average(data), np.std(data)))
mu = np.average(data)
sigma = np.std(data)

# 히스토그램 그려보기
plt.figure()
plt.hist(data)
plt.xlabel('height')
plt.ylabel('frequency')
plt.grid()
plt.show()

# 박스플롯 그려보기
plt.figure()
plt.boxplot(data)
plt.grid()
plt.show()

# 이번엔 정규분포를 따르는 데이터로 가봅시다
# 똑같이 1000개를 추출, 평균과 표준편차는 예전 값 가져다 쓰겠습니다.
data = np.random.normal(mu, sigma, 1000)

# 정규분포를 그려볼께요
plt.figure()
plt.hist(data, 50, normed=1)
plt.xlabel('height')
plt.ylabel('probability')
plt.grid()
plt.show()
