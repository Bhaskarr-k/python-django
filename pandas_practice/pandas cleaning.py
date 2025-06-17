import pandas as pd
df=pd.read_csv("C:\\Users\\LENOVO\\Desktop\\csv files\\smartphones.csv")
new_df=df.dropna()
print(new_df.to_string())
