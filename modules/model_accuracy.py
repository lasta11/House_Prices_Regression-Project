#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def model_accuracy_bar(score1, score2, score3):
    models=['Random Forest','Linear Regression','Light Gradient Boosting Regressor']
    score=[score1, score2, score3]
    plt.bar(models,score)
    plt.title("Machine Learning Models Score comparison")
    plt.xlabel("Machine Learning Model")
    plt.ylabel("Scores")
    plt.show()
    

