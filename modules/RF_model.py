#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def RF_model(df_test,df_train):
    x_train=df_train.drop(columns='SalePrice')
    y_train= df_train['SalePrice']
    x_test= df_test
    
    
    model_randomForest= RandomForestRegressor(random_state= 50)
    train_randomForest= model_randomForest.fit(x_train,y_train)
    prediction_sales= model_randomForest.predict(x_test)
    score_RFM= model_randomForest.score(x_train,y_train)
    print(score_RFM)
    
    return prediction_sales

    

