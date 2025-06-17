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


# import pandas as pd
# d = pd.read_csv("C:\\Users\\LENOVO\\Desktop\\smartphones.csv")
# df=pd.DataFrame(d)

# import pandas as pd

# df = pd.read_csv("C:\\Users\\LENOVO\\Desktop\\csv files\\smartphones.csv")
# print(df)

# to store entire csv file
# import pandas as pd
# df=pd.read_csv("C:\\Users\\LENOVO\\Desktop\\csv files\\smartphones.csv")
# print(df.to_string())


# to store maximum rows
import pandas as pd
pd.options.display.max_rows=100
df=pd.read_csv("C:\\Users\\LENOVO\\Desktop\\csv files\\smartphones.csv")
# df=pd.read_csv("C:\\Users\\LENOVO\\Desktop\\csv files\\smartphones.csv")
print(df.to_string())