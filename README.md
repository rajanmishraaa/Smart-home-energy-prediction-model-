# Smart Home Energy Prediction Model

A supervised machine learning project that predicts household energy consumption using household and environmental features. The project compares Linear Regression, Polynomial Regression, and Ridge Regression models, with cross-validation and Grid Search for model optimization. The final model is deployed using Flask.

## Project Overview

The goal of this project is to predict household energy consumption in kWh based on factors such as:

- Household size
- Average temperature
- Air conditioning availability
- Peak-hour energy usage
- Day of the month
- Day of the week
- Weekend/weekday

## Dataset

The dataset contains 90,000 records of household energy consumption for April 2025.

### Features

| Feature | Description |
|---|---|
| Household_ID | Unique household identifier |
| Date | Date of the energy usage record |
| Energy_Consumption_kWh | Target variable |
| Household_Size | Number of people in the household |
| Avg_Temperature_C | Average daily temperature |
| Has_AC | Whether the household has air conditioning |
| Peak_Hours_Usage_kWh | Energy consumed during peak hours |

The `Date` column was used to create additional features such as day, day of week, and weekend status. `Household_ID` was excluded from model training.

## Machine Learning Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Regression Models
   ↓
Cross-Validation
   ↓
Grid Search
   ↓
Final Model
   ↓
Flask Deployment


Models Used
1. Multiple Linear Regression

Used as the baseline regression model for predicting energy consumption.

2. Polynomial Regression

Used to capture nonlinear relationships between the input features and energy consumption.

3. Ridge Regression

Used with regularization to reduce the effect of multicollinearity and improve model stability.

Model Evaluation

The models were evaluated using:

Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score

5-fold cross-validation and Grid Search were also used for model validation and hyperparameter tuning.

Final Model Performance
Metric	Result
MSE	0.6200
RMSE	0.7874
R² Score	0.9798
Best Ridge Alpha	1
Cross-Validation R²	0.9794

The final Ridge Regression model achieved an R² score of 0.9798 on the test set.

Deployment

The trained model is saved as:

energy_model.pkl

A Flask web application loads the trained model and allows users to enter household information to receive a predicted energy consumption value.

Run the Application

Install the required dependencies:

pip install -r requirements.txt

Run the Flask application:

python app.py

Open the application at:

http://127.0.0.1:5000
Project Structure
Smart-home-energy-prediction-model/
│
├── data/
│   └── household_energy_consumption.csv
│
├── templates/
│   └── index.html
│
├── app.py
├── energy_model.pkl
├── energy_prediction.ipynb
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Flask
Joblib
Jupyter Notebook
