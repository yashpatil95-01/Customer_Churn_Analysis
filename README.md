# 📞 Customer Churn Analysis

A simple yet effective **logistic regression** model to predict customer churn for a telecom company, based on the [Telco Customer Churn dataset] from Kaggle.
```
https://www.kaggle.com/datasets/blastchar/telco-customer-churn
```

---
## 📋 Project Overview

Customer churn prediction helps businesses understand which customers are likely to leave their service. This allows proactive retention strategies and improves revenue.

This project:
- Loads and explores the dataset  
- Prepares data by encoding churn labels  
- Trains a logistic regression classifier  
- Evaluates the model using classification metrics  
- Visualizes churn distribution against customer tenure  

---

## 🚀 How to Run

1. Clone this repo or download the code files.  
2. Download the dataset from Kaggle [here](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and place the CSV file in the `data/` folder.  
3. Install required Python libraries if you haven’t already:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```
Run the main script:
```bash
python churn_analysis.py
```

📊 Results
Classification report printed in console shows precision, recall, and F1-score.

Boxplot visualizes customer tenure vs. churn status.

The plot is saved automatically as results/tenure_vs_churn.png.

🛠️ Technologies & Libraries
Python 3.x

pandas

matplotlib

seaborn

scikit-learn

🔗 Dataset
Telco Customer Churn

Contains customer demographics, service details, and churn labels.

📬 Contact
Questions or feedback? Feel free to reach out!

Happy analyzing! 🚀📈
