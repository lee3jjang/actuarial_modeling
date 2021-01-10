import os
import numpy as np
from scipy.stats import lognorm, gamma, nbinom, poisson

# data 폴더 생성
if not any([s == 'data' for s in os.listdir('.')]): os.mkdir('data')

# 심도 기초데이터 생성
np.random.seed(20210103)
# severity = lognorm(s=1, loc=0, scale=10000)
severity = gamma(a=15, loc=0, scale=10000)
data = severity.rvs(10000).round().astype(int)
np.savetxt('data/claim.csv', data, fmt='%d', delimiter=',')

# 빈도 기초데이터 생성
np.random.seed(20210109)
earned_premium_by_fy = [1000000, 2000000, 1500000, 3000000, 4000000]
# data = [nbinom(n=exposure*3, p=0.3).rvs() for exposure in earned_premium_by_fy]
data = [poisson(mu=exposure*4.5/1e6).rvs() for exposure in earned_premium_by_fy]
data = np.c_[earned_premium_by_fy, data]
np.savetxt('data/num_of_claims.csv', data, fmt='%d', delimiter=',')