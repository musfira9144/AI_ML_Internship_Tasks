#  Task 3: Heart Disease Prediction (Classification)

###  Internship:
AI/ML Engineering Intern — DevelopersHub Corporation  


---

##  Objective
The objective of this task is to build a **machine learning model** that predicts whether a patient is at risk of **heart disease** based on medical attributes such as age, cholesterol, chest pain type, blood pressure, and more.

This is a **binary classification problem**:
- `1` → Heart disease present  
- `0` → No heart disease  

---

##  Dataset
- **Name:** Heart Disease UCI Dataset  
- **Source:** Kaggle  
- **File Used:** `heart.csv`  
- **Rows:** 303 patients  
- **Columns:** 14 medical attributes + target  

### Key Features:
- `age` — age of patient  
- `sex` — 1: male, 0: female  
- `cp` — chest pain type  
- `trestbps` — resting blood pressure  
- `chol` — cholesterol  
- `fbs` — fasting blood sugar  
- `restecg` — resting ECG results  
- `thalach` — max heart rate  
- `exang` — exercise induced angina  
- `oldpeak` — ST depression  
- `ca` — number of major vessels  
- `thal` — thalassemia  
- `target` — 1 (disease), 0 (no disease)  

---

## Technologies Used
- Python  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- Google Colab  

---

##  Steps Performed

###  1. Data Loading  
Imported the `heart.csv` dataset using pandas.

###  2. Data Inspection  
- Checked shape, column names, and data types  
- No missing values found  
- All features numeric → no encoding required  

###  3. Exploratory Data Analysis (EDA)
- Histograms for feature distribution  
- Correlation heatmap to identify important features  
- Observations about medical patterns  

###  4. Train/Test Split  
Split data into:
- 80% training  
- 20% testing  

###  5. Model Training  
Used **Logistic Regression** (best for explainable medical predictions).

###  6. Evaluation Metrics  
Generated:
- Accuracy  
- Confusion Matrix  
- Precision, Recall, F1-score  
- ROC Curve  
- AUC Score  

---

##  Model Performance

| Metric | Score |
|--------|--------|
| **Accuracy** | 0.87 |
| **AUC Score** | 0.93 |
| **Precision (Class 1)** | 0.88 |
| **Recall (Class 1)** | 0.88 |

### Confusion Matrix:
- True Positives (TP): correct predictions of disease  
- True Negatives (TN): correct predictions of no disease  
- False Positives (FP) and False Negatives (FN): low  

---

##  Key Insights

- The Logistic Regression model shows **strong performance**, achieving **87% accuracy**.  
- AUC score of **0.93** indicates the model is excellent at separating healthy vs diseased patients.  
- Most influential features:  
  - chest pain type (`cp`)  
  - maximum heart rate (`thalach`)  
  - ST depression (`oldpeak`)  
  - exercise-induced angina (`exang`)  
  - number of major vessels (`ca`)  
- Dataset was clean and balanced, improving model stability.  
- Model can help with early risk identification, but should not replace medical diagnosis.

---

## 📁 Files Included
Task3_Heart_Disease_Prediction/
├── Task3_Heart_Disease_Prediction.ipynb
└── README.md






---

## 🧑‍💻 Author
**Name:** MUSFIRA  
**Internship Program:** DevelopersHub Corporation — AI/ML Engineering Intern  
**GitHub:** https://github.com/musfira9144

