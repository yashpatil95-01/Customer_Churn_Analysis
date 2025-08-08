# Customer Churn Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
df = pd.read_csv("E:/PythonProjects/PA-Projects/Customer_Churn_Analysis/data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Preview data
print("First 5 rows:\n", df.head())
print("\nChurn distribution:\n", df['Churn'].value_counts())  # Capital 'C'

# Convert 'Churn' to numeric
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})  # Capital 'C'

# Feature selection
X = df[['tenure', 'MonthlyCharges']]  # Note: Column names are case-sensitive here too
y = df['Churn']  # Capital 'C'

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Visualize churn vs. tenure
sns.boxplot(data=df, x='Churn', y='tenure')  # Capital 'C'
plt.title('Tenure vs Churn')
plt.savefig('E:/PythonProjects/PA-Projects/Customer_Churn_Analysis/results/tenure_vs_churn.png')
plt.show()
