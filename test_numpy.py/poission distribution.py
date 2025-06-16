# from numpy import random
# x=random.poisson(lam=2,size=5)
# print(x)



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.poisson(lam=2,size=15))
plt.show()