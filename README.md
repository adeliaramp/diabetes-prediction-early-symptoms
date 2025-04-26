# 🩺 Diabetes Prediction from Early Symptoms

Predicting diabetes risk based on early symptoms using machine learning models.  
This project includes **exploratory data analysis (EDA)**, **feature engineering**, **model comparison**, **cross-validation with confidence intervals**, and an interactive **Streamlit web app** for real-time predictions.

---

## 📚 Table of Contents
- [About the Project](#-about-the-project)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Models Trained](#-models-trained)
- [Evaluation Metrics](#-evaluation-metrics)
- [App Demo](#-app-demo)
- [How to Run the App Locally](#-how-to-run-the-app-locally)
- [Future Improvements](#-future-improvements)
- [Contact](#-contact)

---

## 🧠 About the Project

Diabetes is a major health concern worldwide.  
Early detection through symptoms can help in fast diagnosis and early treatment.

In this project, I built and compared multiple models to predict diabetes risk **using only early symptoms and demographic data** — no lab tests required.

---

## 🗂️ Project Structure

```
diabetes-prediction-early-symptoms/
├── notebooks/
│   └── diabetes_prediction_notebook.ipynb
├── models/
│   ├── diabetes_model_rf.pkl
│   ├── diabetes_model_xgb.pkl
│   ├── diabetes_model_logistic.pkl
│   └── feature_names.pkl
├── app.py
├── requirements.txt
└── README.md
```



---

## 🛠️ Technologies Used
- Python
- Streamlit
- Scikit-learn
- XGBoost
- Pandas
- Matplotlib
- Joblib

---

## 🤖 Models Trained

| Model                | Description                                 |
|:---------------------|:--------------------------------------------|
| Logistic Regression  | Simple, interpretable baseline model        |
| Random Forest        | High-performance ensemble model             |
| XGBoost              | Gradient-boosted trees model, excellent for tabular data |

✅ **Final model selected**: Random Forest (highest recall, best cross-validation performance).

---

## 📊 Evaluation Metrics

| Metric            | Logistic Regression | Random Forest | XGBoost |
|:------------------|:---------------------|:--------------|:--------|
| Accuracy          | 93%                  | 99%           | 98%     |
| Precision         | 98%                  | 100%          | 100%    |
| Recall            | 91%                  | 98%           | 97%     |
| F1-Score          | 94%                  | 99%           | 98%     |
| ROC AUC           | 0.99                 | 1.00          | 1.00    |
| CV Accuracy       | -                    | 98% ± 3%      | 97% ± 3%|
| 95% CI (Accuracy) | -                    | [95.39%, 99.99%] | [93.98%, 99.48%] |

---

## 🌎 App Demo
In the app:
- Users input their symptoms
- Click **Predict**
- See real-time prediction whether they are likely diabetic

---

## ⚙️ How to Run the App Locally

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/diabetes-prediction-early-symptoms.git
    cd diabetes-prediction-early-symptoms
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

4. The app will open automatically in your browser at `http://localhost:8501/` 🎯

---

## 🚀 Future Improvements
- Deploy the app live on Streamlit Cloud
- Add SHAP explainability for more transparent model decisions
- Expand dataset for broader generalization
- Enable users to select between Random Forest, XGBoost, and Logistic Regression inside the app

---

## 📬 Contact

If you'd like to discuss this project or collaborate, feel free to connect! 🚀
