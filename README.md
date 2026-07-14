# AI Customer Retention Assistant

An end-to-end AI-powered customer retention application that predicts customer churn and provides intelligent retention recommendations using Machine Learning and an LLM-powered LangGraph agent.

---

## Project Overview

Customer churn is a major challenge for telecom companies. This project combines Machine Learning with an AI Agent to help customer support teams identify customers at risk of leaving and recommend suitable retention strategies.

The application allows users to:

- Retrieve customer information
- Predict customer churn probability
- Explain churn risk factors
- Recommend retention offers
- Interact using natural language through an AI assistant

---

## Features

### Machine Learning

- Data Quality Assessment & Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Logistic Regression Model
- Random Forest Model
- Model Evaluation
- Exported Scikit-Learn Pipeline

### AI Agent

Built using **LangGraph** and **OpenAI GPT**.

The agent can:

- Lookup customer information
- Predict churn
- Explain risk factors
- Recommend retention offers
- Respond using natural language

### Web Application

- Django Backend
- HTML/CSS Frontend
- Interactive Chat Interface
- Mock Customer Repository
- Modular Service Architecture

---

# Project Architecture

```
                    User
                      │
                      ▼
               Django Web UI
                      │
                      ▼
                Django Views
                      │
                      ▼
              LangGraph Agent
                      │
      ┌───────────────┼───────────────┐
      ▼               ▼               ▼
Lookup Customer   Predict Churn   Retention Offer
      │               │               │
      └───────────────┼───────────────┘
                      ▼
              Scikit-Learn Model
```

---

# Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| Backend | Django |
| Frontend | HTML, CSS, JavaScript |
| Machine Learning | Scikit-Learn |
| Explainability | SHAP |
| Agent Framework | LangGraph |
| LLM | OpenAI GPT |
| Model Serialization | Joblib |
| Deployment | PythonAnywhere |

---

# Project Structure

```
customer-retention-ai/

│
├── notebooks/
│   ├── 01_data_quality_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_model_training.ipynb
│
├── retention/
│   ├── agent/
│   │   ├── graph.py
│   │   ├── nodes.py
│   │   ├── prompts.py
│   │   ├── state.py
│   │   └── tools.py
│   │
│   ├── ml/
│   │   ├── predictor.py
│   │   ├── explain.py
│   │   └── features.py
│   │
│   ├── services/
│   │   ├── customer_repository.py
│   │   ├── customer_service.py
│   │   └── offer_service.py
│   │
│   ├── templates/
│   ├── static/
│   ├── views.py
│   └── urls.py
│
├── saved_models/
│   └── churn_model.pkl
│
├── dataset/
├── requirements.txt
├── README.md
└── manage.py
```

---

# Machine Learning Pipeline

1. Data Cleaning
2. Missing Value Handling
3. Feature Engineering
4. Train/Test Split
5. Data Preprocessing Pipeline
6. Logistic Regression
7. Random Forest
8. Model Evaluation
9. Export Model

---

# AI Agent Workflow

```
User Query
     │
     ▼
LangGraph Agent
     │
     ▼
Tool Selection
     │
     ├── Lookup Customer
     ├── Predict Churn
     └── Recommend Offer
     │
     ▼
LLM Response
```

---

# Sample Queries

```
Predict churn for customer CUST1002
```

```
Why is customer CUST1005 considered high risk?
```

```
Recommend a retention strategy for customer CUST1003
```

```
Summarize customer CUST1001
```

```
Analyze customer CUST1008
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
cd customer-retention-ai
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file

```
OPENAI_API_KEY=your_api_key
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Run Application

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# Example Question

```
Analyze customer CUST1002

Why is customer CUST1002 high risk?

Recommend a retention strategy for CUST1005.

Summarize customer CUST1003.

Predict churn for customer CUST9999.
```

---

# Example Response

```
Customer: John Smith

Prediction:
- No Churn

Probability:
- 41.98%

Risk Level:
- Medium

Risk Factors:
- Low Satisfaction
- Short Tenure
- Month-to-Month Contract

Recommended Offer:
- 10% Loyalty Discount
- Priority Support
- Extra Data
```

---

# Model Evaluation

Models evaluated:

- Logistic Regression
- Random Forest

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

The best-performing model (Logistic Regression) was exported as a Scikit-Learn pipeline and integrated into the AI agent.

---

# Future Improvements

- Persistent customer database
- User authentication
- Conversation memory
- Real-time customer APIs
- SHAP explanations integrated directly into the agent
- Deployment using Docker/Kubernetes
- Monitoring and analytics dashboard

---

# Author

**SHUBHAM KUMAR**

Python Full Stack & AI Developer

GitHub: https://github.com/imusr

LinkedIn: https://www.linkedin.com/in/shubham-kumar-bb4b3a175/

---
