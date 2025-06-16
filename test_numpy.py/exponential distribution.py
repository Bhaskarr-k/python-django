# from numpy import random
# x=random.exponential(scale=2,size=(2,3))
# print(x)

# visualization off exponential distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.exponential(size=1000),kind="kde")
plt.show()