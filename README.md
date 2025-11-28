# AI/ML Engineering Internship Tasks 
**Developer:** Musfira Fiaz  
**Organization:** DevelopersHub Corporation  
**Due Date:** 28th November 2025  

This repository contains my completed tasks for the AI/ML Engineering Internship at DevelopersHub Corporation. The projects demonstrate skills in data preprocessing, visualization, regression, classification, and conversational AI using real-world datasets and models.

---

## Table of Contents
- Task1_Iris_EDA
- Task2_Stock_Price_Prediction
- Task3_Heart_Disease_Prediction
- Task4_Health_Chatbot
- Task6_House_Price_Prediction


---

## Task 1: Exploring and Visualizing a Simple Dataset
**Objective:**  
Load, inspect, and visualize a dataset to understand data trends and distributions.

**Dataset:** Iris Dataset (CSV / via Seaborn)

**Key Steps & Skills:**  
- Loaded dataset using `pandas`  
- Performed data inspection with `.head()`, `.info()`, and `.describe()`  
- Visualized relationships using scatter plots, histograms, and box plots  
- Tools: `matplotlib`, `seaborn`  

**Findings:**  
- Identified feature distributions and correlations  
- Detected outliers and patterns in the dataset  

---

## Task 2: Predict Future Stock Prices (Short-Term)
**Objective:**  
Predict the next day’s stock closing price using historical data.

**Dataset:** Stock market data from Yahoo Finance (`yfinance` library)

**Key Steps & Skills:**  
- Fetched historical stock data for selected companies  
- Preprocessed features: Open, High, Low, Volume  
- Trained regression models: Linear Regression and Random Forest  
- Plotted actual vs predicted prices  

**Key Results:**  
- Regression models provide short-term price trend predictions  
- Visual comparison shows reasonable prediction accuracy for next-day closing prices  

---

## Task 3: Heart Disease Prediction
**Objective:**  
Predict whether a person is at risk of heart disease based on health metrics.

**Dataset:** Heart Disease UCI Dataset (Kaggle)

**Key Steps & Skills:**  
- Cleaned data and handled missing values  
- Performed Exploratory Data Analysis (EDA)  
- Trained classification models: Logistic Regression, Decision Tree  
- Evaluated using accuracy, confusion matrix, and ROC curve  
- Analyzed feature importance  

**Key Results:**  
- Identified key health features affecting heart disease risk  
- Classification models achieved good predictive performance  

---

## Task 4: General Health Query Chatbot
**Objective:**  
Create a chatbot to answer general health-related questions using a large language model and deployed it on streamlit.

**Tools:** openai/gpt-oss-120b API ,llama-3.1-8b-instant.

**Key Steps & Skills:**  
- Built Python script to send queries to an LLM  
- Applied prompt engineering for friendly and clear responses  
- Added safety rules to prevent harmful advice  
- Sample queries tested: “What causes a sore throat?”
- Deployed the chatbot using streamlit.

**Key Results:**  
- The chatbot provides reliable general health information  
- Responses are safe, informative, and user-friendly  

---

## Task 6: House Price Prediction
**Objective:**  
Predict house prices based on property features like size, bedrooms, and location.

**Dataset:** House Price Prediction Dataset (Kaggle)

**Key Steps & Skills:**  
- Preprocessed features including square footage, bedrooms, and location  
- Trained regression models: Linear Regression, Gradient Boosting  
- Visualized predicted vs actual prices  
- Evaluated model performance using MAE and RMSE  

**Key Results:**  
- The model accurately predicts housing prices based on key features  
- Visualizations confirm prediction reliability  

---

## Tools & Libraries Used
- Python, Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- yfinance (for stock data)  
- OpenAI GPT API / Hugging Face models  
- Jupyter Notebook
- GroqCloud
- Kaggle 

---

## Notes
- Each task is self-contained in its respective folder
- Clear explanations, visualizations, and model evaluations are included  
- Safe and ethical AI/ML practices followed for chatbot tasks  

