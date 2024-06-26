## Authors
[Sumbati Lindah](mailto:sumbatilinda@gmail.com)

# Bengaluru House Price Prediction

***Demo of the server.py***


![House Price Prediction Demo](https://github.com/Sumbati10/BANGALORE_HOUSE_PREDICTION/blob/main/DEMO/demo_Bengaluru.gif)

<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/><img alt="Pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" /><img alt="NumPy" src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" /><img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" />

### Description of the project:
This data science project series walks through step by step process of how to build a real estate price prediction website.  I will first build a model using sklearn and linear regression using bangaluru housing prices dataset from kaggle.com. Second step would be to write a python flask server that uses the saved model to serve http requests.  Third component is the website built in html, css, bootstrap and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price. During model building I will cover data science concepts such as data loading and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc.

Data Collection - From Kaggle: https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

**Methodology / Approach**

My methodology for solving the problem of predicting home prices accurately in Bangalore involves leveraging the power of data and advanced machine learning techniques. The project follows a robust data science process, including data loading and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, and hyperparameter tuning using GridSearchCV and k-fold cross-validation.

I have used Python as the primary programming language for developing the machine learning models libraries for optimized performance. The models built and trained were Linear Regression, Lasso, Decision Tree, Random forest, AdabOOST regression,  with the highest accuracy being the Random Forest model. Therefore, the Random forest regression model has been selected as the final model for prediction.

Additionally, I have used several other standard libraries such as pandas, numpy, flask, request, and matplotlib.

To make the project more user-friendly, I have developed a sleek and intuitive user interface using HTML, CSS, and JavaScript. The user interface allows users to input the necessary features and receive an instant price prediction.

Furthermore, we have used a Flask server to consume the trained machine learning model and expose HTTP endpoints for various requests, enabling seamless integration with other applications and systems. I have also used a pickle file to store the trained model, making it easy to deploy and use in various environments.

Overall, the methodology involves using advanced machine learning techniques, optimized libraries, and a user-friendly interface to develop a robust and efficient solution for predicting home prices accurately in Bangalore. My approach demonstrates the power of data science in solving real-world problems and provides a framework for developing similar machine-learning applications.


1. Python
2. Numpy and Pandas for data cleaning
3. Matplotlib for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI

## EDA
<img width="541" alt="image" src="https://github.com/Sumbati10/BANGALORE_HOUSE_PREDICTION/assets/105505214/45d301c0-f20a-4ee7-ad67-1a31bbbf64ee">
<img width="548" alt="image" src="https://github.com/Sumbati10/BANGALORE_HOUSE_PREDICTION/assets/105505214/5ab43fe4-4597-481d-a592-22ad04bb6fe4">

## MODEL 
Linear Regression
Lasso
Decision Tree
Random forest
AdabOOST regression
And others 

Considering the bias variance trade-off and the evaluation metrics, the best performing model was Random Forest Regression with optimized parameters.

<img width="382" alt="image" src="https://github.com/Sumbati10/BANGALORE_HOUSE_PREDICTION/assets/105505214/4cfc881e-d1a8-4308-88b1-253baae492f9">


## Run this project locally

To run this project on your local machine:
1. Clone the run-locally branch OR download zip file
```
git clone https://github.com/Sumbati10/BANGALORE_HOUSE_PREDICTION.git
```
2. Change to the server directory
```
cd server
```
3. Install the requirements
```
pip install requirements.txt
```
4. Run the server
```
python server.py
```
<img width="950" alt="image" src="https://github.com/Sumbati10/BANGALORE_HOUSE_PREDICTION/assets/105505214/a824791b-a4e8-4711-af37-71f07f668e6f">



## Conclusion

This is a complete end-to-end project from data cleaning, EDA, model selection to deploying and creating UI. While choosing models, GridSearchCV was used along with k-fold cross validation. In this, **Random Forest Regression** gave the best accuracy.


<img width="410" alt="image" src="https://github.com/Sumbati10/BANGALORE_HOUSE_PREDICTION/assets/105505214/caafb686-6d56-424c-b687-78dcd78ec72f">


Flask API endpoints were created to fetch the list of locaitons and to predict the results.

# Pattent Rights

- This work is entirely the intelectual property of the **AUTHOR**: Lindah Sumbati
- However, use of the files and the code is allowed for all. Enjoy your learning!
   

