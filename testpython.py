import pandas as pd
data = [{1,2},{5,6,7}]
df = pd.DataFrame(data,index=['first','second'],columns=['a','b','c'])
print (df)
df.loc['first','c']=5
print(df)
