#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def missing_values(df):
    NaN_column= []
    for i in df.columns:
        if df[i].isnull().sum()>1 :
            NaN_column.append(i)
    
    NaN_found= df.isnull().sum()/df.shape[0]*100
    remove_column= NaN_found[NaN_found>20].keys()
    df.drop(columns=remove_column, inplace= True)
    values= df.select_dtypes(include=['float64','int64'])
    NaN_values=[]
    for j in values:
        if values[j].isnull().sum()>0 :
            NaN_values.append(j)
    df.fillna(values.mean(),inplace= True)
    df.fillna(method= 'ffill', inplace= True)
    

