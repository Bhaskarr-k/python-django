# import pandas as pd
# a=[1,2,3,4]
# myvar=pd.Series(a[3])
# print(myvar)


# create labels
# import pandas as pd
# a=[1,5,6]
# myvar=pd.Series(a,index=['x','y','z'])
# print(myvar)


# key and values as a series
# import pandas as pd
# calories={'basu':23,'bhaskar':25,'siva':29}
# myvar=pd.Series(calories)
# print(myvar)


# import pandas as pd
# a=[1,2,3]
# myvar=pd.Series(a,index=['x','y','z'])
# print(myvar)


import pandas as pd
calories={'basu':23,'bhaskar':25,'siva':35}
myvar=pd.Series(calories)
print(myvar.iloc[23])