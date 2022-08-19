#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def plot_graph(predictions_1,prediction_2, prediction_3):
    plt.figure(figsize=(15,8))
    plt.plot(predictions_1,color='indianred', label="Price prediction using Random Forest Model" )
    plt.plot(prediction_2,color='khaki', label="Price prediction using Linear Regression Model")
    plt.plot(prediction_3,color='skyblue', label="Price prediction using Light Gradient Boosting Regressor Model")
    plt.legend()
    plt.ylabel('Price')
    plt.xlabel('House Number' )
    plt.title ("House prediction using Machine learning Models")
    plt.show()
    

