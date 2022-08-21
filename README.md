# House-Price-Predictor

House Price Predictor Engine made with Python for Training Machine Learning Model & Flask for making Web Application to represent the Data.

It is made by using DataBase of 13321 Houses of Bangalore.

Website Link: https://house--price-predictor.herokuapp.com/

Algorithms used are:
* Linear Regression
* Lasso Regression
* Ridge Regression
* ElasticNet Regression

R2 Scores:
* No Regularization :  0.8295831047989525
* Lasso Regularization :  0.8199181874762704
* ElasticNet Regularization :  0.7728405046673602 (Worst)
* Ridge Regularization :  0.8296651410179725 (Best)

Libraries used are:
* For Training Model:
  * Numpy
  * Pandas
  * SciKit Learn
  * Seaborn
  * Pickle
* For Web Development:
  * Flask
  * Flask_Cors
  * Bootstrap
* For Integrating ML Model to WebApp:
  * Jinja2 Templating Engine
  
 IDE Used:
 * Jupyter Notebook for Exploratory Data Analysis (EDA)
 * VS Code for developing Flask Web App
 
 Server Used for Deployement: Gunicorn
 
 DataSet Link: https://www.kaggle.com/code/nehahatti/bangalore-house-price-prediction/data
