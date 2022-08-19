#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def visualize_bar(df):
    numeric_column= df.select_dtypes(include=['int64','float64'])
    drop_ID_SalePrice= numeric_column.drop(['Id','SalePrice'],axis=1)
    for i in drop_ID_SalePrice:
        plt.bar(df[i],df['SalePrice'],color="orange")
        plt.xlabel(i)
        plt.ylabel("Sales Price")
        plt.title("Sales Price Vs."+i)
        plt.show() 
def visualize_scatter(df):
    numeric_column= df.select_dtypes(include=['int64','float64'])
    category_column= df.select_dtypes(include=['object'])
    drop_ID_SalePrice= numeric_column.drop(['Id','SalePrice'],axis=1)
    for i in drop_ID_SalePrice:
        sns.scatterplot(data= df, y='SalePrice',x= i)
        
        
        #plt.scatter(df[i],df['SalePrice'],color="green")
        #plt.xlabel(i)
        #plt.ylabel("Sales Price")
        plt.title("Sales Price Vs."+i)
        plt.show() 
    for j in category_column:
        sns.barplot(x=j, y='SalePrice',data=df)
        plt.title("Sales Price Vs."+j)
        
def heat_map(df):
    plt.figure(figsize=(20,20))
    sns.heatmap(df.corr())
    

