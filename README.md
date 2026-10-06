# 🏠 House Price Prediction — Regression & Classification

## 📌 Project Overview

This project uses Machine Learning to predict house prices and classify houses into **Low Price** and **High Price** categories.

The project uses the **California Housing Dataset** and implements both regression and classification techniques using Scikit-learn.

## 🎯 Objectives

* Predict the estimated price of a house.
* Classify houses as Low Price or High Price.
* Compare multiple Machine Learning algorithms.
* Build an interactive web application using Streamlit.

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

## 🤖 Machine Learning Models

### Regression

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

**Best Model:** Random Forest Regressor

**R² Score:** 0.805

### Classification

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

**Best Model:** Random Forest Classifier

**Accuracy:** 89.39%

## 📊 Dataset

The project uses the California Housing Dataset provided by Scikit-learn.

The dataset contains features such as:

* Median Income
* House Age
* Average Rooms
* Average Bedrooms
* Population
* Average Occupancy
* Latitude
* Longitude

## 🌐 Web Application

The project includes a Streamlit web application where users can enter house details and receive:

* Predicted house price
* Price category

## 📁 Project Structure

```text
House_Price_Prediction/
│
├── app.py
├── house_price_prediction.ipynb
├── house_price_regression_model.pkl
├── house_price_classification_model.pkl
├── README.md
└── .gitignore
```

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib streamlit
```

### 2. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in the browser.

## 📈 Results

| Task           | Best Model    |       Performance |
| -------------- | ------------- | ----------------: |
| Regression     | Random Forest |        R² = 0.805 |
| Classification | Random Forest | Accuracy = 89.39% |

## 🚀 Future Improvements

* Add advanced hyperparameter tuning.
* Add more interactive visualizations.
* Deploy the application online.
* Add model prediction confidence.
* Improve the user interface.

## 👩‍💻 Author

**Rithiga RT**

IT Student | Python Developer | AI Aspirant
