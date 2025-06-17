import pandas as pd
data = {
    "duration":{'0':6,'1':7,'2':8},
    "pulse":{'0':6,'1':7,'2':8},
    "calories":{'name':'basu','age':25,'course':'python'}
}
df=pd.DataFrame(data)
print(df)