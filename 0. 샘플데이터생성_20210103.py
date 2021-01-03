import os
import numpy as np
from scipy.stats import lognorm, gamma

# data 폴더 생성
if not any([s == 'data' for s in os.listdir('.')]): os.mkdir('data')

# 기초데이터
np.random.seed(20210103)
# loss = lognorm(s=1, loc=0, scale=10000)
loss = gamma(a=15, loc=0, scale=10000)
data = loss.rvs(10000).round().astype(int)
np.savetxt('data/claim.csv', data, fmt='%d', delimiter=',')