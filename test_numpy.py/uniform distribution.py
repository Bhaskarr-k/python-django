# from numpy import random
# x=random.uniform(size=(2,3))
# print(x)



from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.uniform(size=100),kind="kde")
plt.show()