# Create Database

CREATE DATABASE churn_analysis;


# Use the database:

USE churn_analysis;

# Create Table

CREATE TABLE churn_data (
    tenure INT,
    MonthlyCharges FLOAT,
    TotalCharges FLOAT,
    Churn INT,
    CLV FLOAT,
    RiskScore INT,
    RiskLevel VARCHAR(20),
    CLV_Segment VARCHAR(20),
    Contract_Type VARCHAR(20)
);

# Import CSV from PowerShell

# Load CSV File

LOAD DATA LOCAL INFILE 'C:/path/to/churn_sql_dataset.csv'
INTO TABLE churn_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Example:
'C:/Users/Lenovo/customer-churn-revenue-intelligence/data/processed/churn_sql_dataset.csv'

# Check Data Loaded 

SELECT * FROM churn_data LIMIT 10;

# Run Your SQL Analysis

SELECT 
COUNT(*) AS total_customers,
SUM(Churn) AS churned_customers,
(SUM(Churn)*100.0/COUNT(*)) AS churn_rate
FROM churn_data;

# Churn by Contract


SELECT 
Contract_Type,
COUNT(*) AS customers,
SUM(Churn) AS churned
FROM churn_data
GROUP BY Contract_Type;

# Revenue at Risk

SELECT 
SUM(CLV) AS revenue_lost
FROM churn_data
WHERE Churn = 1;

# Overall Churn Rate

SELECT 
COUNT(*) AS total_customers,
SUM(Churn) AS churned_customers,
ROUND((SUM(Churn)*100.0/COUNT(*)),2) AS churn_rate_percent
FROM churn_data;

# Churn by Contract Type

SELECT 
Contract_Type,
COUNT(*) AS total_customers,
SUM(Churn) AS churned_customers,
ROUND((SUM(Churn)*100.0/COUNT(*)),2) AS churn_rate
FROM churn_data
GROUP BY Contract_Type
ORDER BY churn_rate DESC;

# Revenue at Risk

SELECT 
ROUND(SUM(CLV),2) AS revenue_lost
FROM churn_data
WHERE Churn = 1;

# Revenue by Customer Segment

SELECT 
CLV_Segment,
ROUND(SUM(CLV),2) AS total_revenue
FROM churn_data
GROUP BY CLV_Segment
ORDER BY total_revenue DESC;

# Risk Level Distribution

SELECT 
RiskLevel,
COUNT(*) AS customers
FROM churn_data
GROUP BY RiskLevel;

# Churn by Risk Level

SELECT 
RiskLevel,
COUNT(*) AS total_customers,
SUM(Churn) AS churned_customers
FROM churn_data
GROUP BY RiskLevel;

# High Value Customers at Risk

SELECT *
FROM churn_data
WHERE CLV_Segment = 'High Value'
AND RiskLevel = 'High Risk';

# Average Customer Value

SELECT 
ROUND(AVG(CLV),2) AS avg_customer_value
FROM churn_data;

# Churn by Tenure Group

SELECT 
CASE 
WHEN tenure < 12 THEN '0-12 months'
WHEN tenure < 24 THEN '12-24 months'
WHEN tenure < 48 THEN '24-48 months'
ELSE '48+ months'
END AS tenure_group,
COUNT(*) AS customers,
SUM(Churn) AS churned
FROM churn_data
GROUP BY tenure_group;


