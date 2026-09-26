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
