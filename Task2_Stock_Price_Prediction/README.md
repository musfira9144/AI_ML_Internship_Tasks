#  Task 2: Predict Future Stock Prices (Short-Term)

###  Internship:
AI/ML Engineering Intern — DevelopersHub Corporation  
 

---

##  Objective
The goal of this task is to predict the **next day's closing price** of a stock using historical financial data.  
We use the `yfinance` API to download stock market data and train a **Linear Regression model**.

---

##  Dataset
- **Stock Used:** Apple (AAPL)  
- **Source:** Yahoo Finance (via `yfinance`)  
- **Data Range:** 2023–2024  
- **Features Used:**
  - Open  
  - High  
  - Low  
  - Volume  

**Target:** Close Price

---

##  Technologies Used
- Python 3  
- pandas  
- numpy  
- yfinance  
- scikit-learn  
- matplotlib  
- seaborn  
- Google Colab / Jupyter Notebook  

---

##  Steps Performed
1. **Downloaded stock data** using `yfinance`  
2. **Inspected dataset** (shape, columns, missing values)  
3. **Selected features** (Open, High, Low, Volume)  
4. **Split data** into training and testing sets  
5. **Trained a Linear Regression model**  
6. **Predicted closing prices** for the test set  
7. **Plotted Actual vs Predicted values**  
8. **Evaluated model** using MAE, RMSE, R²  

---

##  Model Performance
| Metric | Value |
|--------|--------|
| **MAE** | 0.78 |
| **RMSE** | 1.02 |
| **R² Score** | 1.00 |

---

##  Insights
- The model predicts Apple's closing prices **very accurately** because daily variations are small.  
- The most influential features are **Open, High, and Low** prices.  
- Linear Regression works well for stable stock behavior.  
- To improve real-world forecasting, advanced models like **LSTM** or **Gradient Boosting** can be used.

---

##  Files Included 
Task2_Stock_Price_Prediction/
├── Task2_Stock_Price_Prediction.ipynb
└── README.md



---

## 🧑‍💻 Author
**Name:** Musfira  
**Internship Program:** DevelopersHub Corporation — AI/ML Engineering Intern  



