# import pandas as pd
# data={'calaories':[1,2,3],'duration':[0,1,0]}
# df=pd.DataFrame(data)
# # print(df)
# print(df.loc[1])


# named indexes

# import pandas as pd
# data={'calaories':[1,2,3],'duration':[0,1,0]}
# df=pd.DataFrame(data,index=['day1','day2','day3'])
# print(df.loc['day2'])


# # load files into a dataframe
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())