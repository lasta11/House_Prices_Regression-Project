#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def LR_model(df_test,df_train):
    x_train=df_train.drop(columns='SalePrice')
    y_train= df_train['SalePrice']
    x_test= df_test
    
    
    model_lgbRegressor= LGBMRegressor(verbose=1, objective='regression',random_state=50)
    train_lgbRegressor= model_lgbRegressor.fit(x_train,y_train)
    prediction_sales_LGBR= model_lgbRegressor.predict(x_test)
    score_LGBR= model_lgbRegressor.score(x_train,y_train)
    print(score_LGBR)
    
    return prediction_sales_LGBR

    

