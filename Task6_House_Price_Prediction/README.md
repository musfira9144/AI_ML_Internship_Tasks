# Task 6: House Price Prediction

## Overview
This project focuses on predicting house prices using a dataset of 2000 entries with 10 columns. Two regression models were used for prediction and evaluated based on their performance.

## Dataset
- **Number of entries:** 2000  
- **Columns / Features:**
  - `Area`
  - `Bedrooms`
  - `Bathrooms`
  - `Floors`
  - `YearBuilt`
  - `Location` (Rural/Suburban/Urban)
  - `Condition` (Fair/Good/Poor)
  - `Garage` (Yes/No)
- **Target variable:** `Price`
- **Feature shape after preprocessing:** (2000, 12)  
- **Target shape:** (2000,)

## Preprocessing
- One-hot encoded categorical variables (`Location`, `Condition`, `Garage`).
- Checked for missing values and handled appropriately.
- Prepared features and target arrays for model training.

## Models Used
1. **Linear Regression**
2. **Gradient Boosting Regressor**

## Evaluation Metrics
- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Squared Error)**

## Results

| Model               | MAE            | RMSE           |
|--------------------|----------------|----------------|
| Linear Regression   | 243,241.98     | 279,859.73     |
| Gradient Boosting   | 245,325.59     | 283,939.16     |

## Conclusion
- **Linear Regression** performed slightly better in both MAE and RMSE.  
- Recommended model for predicting house prices: **Linear Regression**.

## Notes
- This project demonstrates basic regression modeling and comparison.
- It provides insights into feature importance and model evaluation for structured data.
