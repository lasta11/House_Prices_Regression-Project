# House Prices - Advanced-Regression-Project

This repository holds a project to predict the final price of each home with the datasets from Kaggle Competition using Linear Regression Model and Random Forest Model.

## Overview

* The objective of this project is to predict the final price of residential homes in Iowa, with set of explanatory variables which affect the price change of the houses using machine learning models.
* This repository holds a set of code, that can be used to prepare, explanatory data analysis, train, and predict the prices of houses using Linear Regression and Random Forest Models.

## Summary of Workdone

### Data
* Data:
  * Datasets from Kaggle: [House Prices - Advanced regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)
  * Type: The datasets are in 2 csv files (train and test)
  * Size: Train dataset - 449 KB, Test dataset- 440 KB
  * Attributes: 76 attributes with house details, for example: House ID, Lot size in square feet, Alley, Street, house condition, house-style, year built, exterior design, roof style, land slope, neighborhood, utilities, Lot Shape, Land Condition, Overall quality, Overall condition, external quality, etc.
  * Description: The datasets's attributes are in abbreviation form, along with this repositpry it contains a texfile [description](https://github.com/lasta11/House_Prices_Regression-Project/blob/main/Datasets/data_description.txt) to describe about the attribute of the house.

* Preprocessing/ Clean up:

   * In preparing the data, I firstly counted the number of Missing values or NaN in the both datasets. The attributes having more than 20% missing values were removed, for the data to be more reliable.
   * I then created a function that keeps only the attributes with less than 20% of missing values and missing values were replaced with mean score of the attribute.
   * About, 3 of the attributes were removed for having many missing values.
   * I then created a another function, to separate numeric and categorical values in the datasets.
   * Within the function, the categorical/ object data-types were transformed using LabelEncoder.
 
 * Data Visualization: 
 
     * In this project, using Matplotlib, I have plotted each attribute over the final sale price of the house, to learn how each attribute affects the sales price of the house.
     * Categorical graphs helps us understand the sales price of houses differing from each category of house-type, and area.
     * Correlation graph helps to understand the price difference of houses over various house qualities and types. 

    Here are some examples of data visualization :

      ![pics](https://github.com/lasta11/House_Prices_Regression-Project/blob/main/Example%20images/SaleCondition_bargraph.png)
       ![pics](https://github.com/lasta11/House_Prices_Regression-Project/blob/main/Example%20images/SalesPrice_Vs_AverageBedroom.png)
       ![pics](https://github.com/lasta11/House_Prices_Regression-Project/blob/main/Example%20images/SalesPrice_Vs_House_remodled.png)


 *    Problem Formulation:
    * Machine Learning Model:
        * Input: x, y train sets of data with all attributes of the house properties and history.
        * Output: Predicted sale price of house
        * Used Score()
   
* Training:
    * Training for the datasets for Linear Regression, and Random Forest model were completed within few seconds, while the Light Gradient Bright Regressor took about 3 minutes to completely train the data.
   
* Prediction:

All three machine learning methods used in this project were used to predict the final sale prices of the houses in Iowa. Here are the results:

![pics](https://github.com/lasta11/House_Prices_Regression-Project/blob/main/Example%20images/Comparison%20of%20data.png)


## Conclusions:
With the above data analysis, the predictions from Random Forest and Light Gradient Boosting Regressor have closer and more accurate results than Linear Regression model.From, accuracy score we can tell that Random Forest has the highest accuracy score being 98.198%, and this is the most reliable one among the 3 models used to predict regression price of the houses.

![pics](https://github.com/lasta11/House_Prices_Regression-Project/blob/main/Example%20images/Model_comparison.png)

## Future Work:
  * For further work on this project, I plan to build own machine learning models for future price prediction with regression.
  * I also plan on evaluating RMSE( Root Mean Square Error) for the predictions made to have minimum outliers.
  * I plan to work on finding correlation between each attribute of the dataset with sales price.
  
## How to reproduce results:

 * [modules](https://github.com/lasta11/House_Prices_Regression-Project/tree/main/modules)
    
    * data_preparation.py : function to find the missing values in the datasetm clean the attributes with maximum number of missing values and replace it with mean score. This function will return a ready to use dataset for further analysis or training.
    
    * exploratory_data_analysis.py : function to learn about correlation between the properties of dataset and also separate scatterplots and bargraphs to see the relation between the attributes.
    
    * LGBR_model.py : function to help train the dataset using Light Gradient Boosting Regressor.
    
    * LR_model.py : function to help train the dataset using Linear Regression model.
    
    * RF_model.py : function to help train the dataset using Random Forest Model.
    
    * graph_predicted_models.py : function to visualize the change of house prices with 3 different methods.
 
 * [main.ipynb](https://github.com/lasta11/House_Prices_Regression-Project/blob/main/main.ipynb)
    This notebook will help to guide through each step of this project.
    
 
## Software Setup 
* Package used in notebook: pandas, numpy, matplotlib, pyplot, seaborn, warnings, sklearn
* Dell laptop was used in this programming and training of models.

## References
   * Dataset- https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
  
