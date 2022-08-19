#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def LR_model(df_test,df_train):
    x_train=df_train.drop(columns='SalePrice')
    y_train= df_train['SalePrice']
    x_test= df_test
    
    
    model_linearRegression= LinearRegression()
    train_linearRegression= model_linearRegression.fit(x_train,y_train)
    prediction_sales_LRM= model_linearRegression.predict(x_test)
    score_LRM= model_linearRegression.score(x_train,y_train)
    print(score_LRM)
    
    return prediction_sales_LRM

    

