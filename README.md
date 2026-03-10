# 📉 Customer Churn & Revenue Intelligence Platform

![Python](https://img.shields.io/badge/Python-Data%20Science-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-ScikitLearn-orange)
![SQL](https://img.shields.io/badge/SQL-Analytics-lightgrey)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)

An **end-to-end data analytics and machine learning platform** designed to **identify customers at risk of churn and estimate potential revenue loss**.

The project combines **data analysis, predictive modeling, and business intelligence dashboards** to help organizations proactively **retain customers and protect revenue**.

Built using **Python, SQL, and Power BI**, the system transforms raw telecom customer data into **actionable business intelligence and churn risk predictions**.

---

# 🚀 Project Overview

Customer churn is one of the most critical challenges for **subscription-based businesses**. Losing customers directly impacts **revenue stability and long-term growth**.

This project addresses the churn problem by:

• Analyzing customer behavior patterns
• Predicting churn probability using machine learning
• Estimating revenue at risk due to churn
• Delivering insights through an interactive dashboard

The platform helps organizations answer key business questions:

• Which customers are most likely to churn?
• What factors influence churn the most?
• How much revenue is at risk?
• Which customer segments need retention campaigns?

---

# ⭐ Key Features

## 1️⃣ Churn Prediction Model

A machine learning model predicts the probability that a customer will churn.

Key steps include:

• Feature engineering on demographics and service usage
• Data preprocessing and categorical encoding
• Model training using **Scikit-learn**
• Performance evaluation using classification metrics

---

## 2️⃣ Revenue Risk Analysis

The platform estimates **potential revenue loss caused by churn**.

Key metrics calculated:

• Monthly revenue at risk
• High-value customers likely to churn
• Customer lifetime value indicators

This helps companies prioritize **high-impact retention strategies**.

---

## 3️⃣ Interactive Power BI Dashboard

An interactive **business intelligence dashboard** was built to visualize churn insights.

Dashboard views include:

• Customer churn distribution
• Revenue loss analysis
• Customer segmentation
• Churn probability by contract type
• Churn trends across demographics

---

# 🛠 Tech Stack

| Category           | Tools        |
| ------------------ | ------------ |
| Programming        | Python       |
| Data Processing    | Pandas       |
| Machine Learning   | Scikit-learn |
| Database Querying  | SQL          |
| Data Visualization | Power BI     |

---

# 📊 Dataset

**IBM Telco Customer Churn Dataset**

Dataset characteristics:

• ~7,000 telecom customers
• Customer demographics
• Service subscriptions
• Billing information
• Churn status

Key variables include:

• Customer tenure
• Contract type
• Internet service
• Payment method
• Monthly charges
• Total charges
• Churn label

The interactive Dashboard :
<img width="2767" height="1600" alt="e4f8cdb7-1 (1)" src="https://github.com/user-attachments/assets/72d32987-dd80-4877-8f70-708a407bc63c" />



---

# 🏗 Project Architecture

```
Data Source
   ↓
Data Cleaning & Transformation (Python, Pandas)
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Machine Learning Model (Scikit-learn)
   ↓
SQL Data Aggregation
   ↓
Power BI Dashboard
   ↓
Business Insights & Revenue Risk Analysis
```

This architecture demonstrates a **complete analytics pipeline used in modern data teams**.

---

# 🤖 Machine Learning Workflow

1️⃣ Data preprocessing
2️⃣ Handling missing values
3️⃣ Encoding categorical variables
4️⃣ Feature scaling
5️⃣ Train/test split
6️⃣ Model training
7️⃣ Performance evaluation

Models explored:

• Logistic Regression
• Random Forest (optional extension)

Evaluation metrics:

• Accuracy
• Precision
• Recall
• F1 Score

---

# 📈 Business Insights Generated

The analysis reveals several key churn patterns:

• Customers with **month-to-month contracts churn the most**
• **Higher monthly charges increase churn probability**
• Customers with **longer tenure are less likely to churn**
• Certain **payment methods correlate with higher churn**

These insights help companies:

• Target high-risk customers
• Offer retention incentives
• Promote long-term contracts
• Reduce revenue leakage

---

# 📂 Repository Structure

```
customer-churn-revenue-intelligence
│
├── app.py
├── README.md
│
├── data
│   ├── raw
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   │
│   └── processed
│       ├── cleaned_churn_data.csv
│       ├── churn_sql_dataset.csv
│       └── churn_dashboard_dataset.csv
│
├── notebooks
│   └── churn_analysis.ipynb
│
├── sql
│   └── churn_analysis.sql
│
├── dashboard
│   ├── churn_dashboard.pbix
│   └── powerbi_dashboard.png
│
├── images
│   ├── churn_distribution.png
│   ├── churn_by_contract.png
│   ├── churn_by_tenure.png
│   ├── churn_by_charges.png
│   ├── churn_by_clv.png
│   ├── revenue_vs_churn.png
│   └── risk_level_vs_churn.png
│
└── models

---

# 📊 Example Dashboard Metrics

Key KPIs displayed in the Power BI dashboard:

• Total Customers
• Churn Rate
• Monthly Revenue
• Revenue at Risk
• High-Risk Customer Segments

---

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/CodingWithDevraj/customer-churn-revenue-intelligence.git
cd customer-churn-revenue-intelligence
```

---

### 2. Install Dependencies

Create a virtual environment (recommended) and install required packages.

```bash
pip install -r requirements.txt
```

Required libraries include:

* pandas
* numpy
* scikit-learn
* streamlit
* plotly
* matplotlib
* seaborn

---

### 3. Run Data Analysis Notebook

Open the Jupyter notebook to explore data preprocessing, feature engineering, and machine learning models.

```bash
jupyter notebook notebooks/churn_analysis.ipynb
```

---

### 4. Run the Streamlit Web App

Launch the interactive analytics app locally.

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

### 5. View the Power BI Dashboard

Open the Power BI dashboard file:

```
dashboard/churn_dashboard.pbix
```

using **Power BI Desktop** to explore the interactive visualizations.

---

## Live Demo

You can view the deployed Streamlit application here:

```
https://customer-churn-revenue-intelligence-w5elzw32zutjz2hdfjfnqu.streamlit.app/
```

---




# 🔮 Future Improvements

Possible extensions for the project:

• Deploy churn prediction model as an API
• Build real-time churn monitoring dashboards
• Add customer lifetime value prediction
• Automate data pipelines

---

# ⭐ Project Highlights

• End-to-end data analytics pipeline
• Real-world telecom churn dataset
• Machine learning based churn prediction
• Business-ready Power BI dashboard
• Revenue risk estimation

---

# 👨‍💻 Author

**Devraj Choudhary**

B.Tech – Computer Science & Engineering
Gurukul Kangri Deemed to be University

Interests

• Data Science
• Machine Learning
• Business Intelligence

GitHub
[https://github.com/CodingWithDevraj](https://github.com/CodingWithDevraj)

LinkedIn
[https://www.linkedin.com/in/devraj-choudhary-3889412bb/](https://www.linkedin.com/in/devraj-choudhary-3889412bb/)

---

