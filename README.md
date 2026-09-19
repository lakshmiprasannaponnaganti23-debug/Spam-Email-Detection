# Spam Email Detection

## Project Author

**Lakshmi Prasanna Ponnaganti**

---

## Project Overview

Spam Email Detection is a Machine Learning project that classifies email messages as either **Spam** or **Not Spam**.

The system uses Natural Language Processing (NLP) techniques to convert email text into numerical features and a Machine Learning model to classify the email.

The project also provides a Streamlit web interface where users can paste a complete email and analyze it.

---

## Objectives

- Detect spam emails automatically.
- Classify emails as Spam or Not Spam.
- Apply TF-IDF for text feature extraction.
- Use Logistic Regression for classification.
- Evaluate the model using standard Machine Learning metrics.
- Provide a simple web interface for email analysis.
- Identify additional warning signals such as URLs and suspicious words.

---

## AI Concepts Used

### 1. Machine Learning

Machine Learning is used to learn patterns from previously classified emails and predict the category of new emails.

### 2. Text Classification

The system classifies email text into two classes:

- `0` → Not Spam
- `1` → Spam

### 3. TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts email text into numerical features that can be processed by the Machine Learning model.

### 4. Logistic Regression

Logistic Regression is used as the classification algorithm to predict whether an email is Spam or Not Spam.

### 5. Feature Engineering

The project also performs additional email analysis, including:

- URL detection
- Suspicious word detection
- Email character count

---

## Dataset

The project uses the publicly available **Apache SpamAssassin Public Corpus**.

For this project, the following datasets were used:

- Easy Ham
- Spam

After preprocessing:

- Total emails: **3,052**
- Normal emails: **2,551**
- Spam emails: **501**

---

## Project Workflow

```text
Email Dataset
      ↓
Email Text Extraction
      ↓
Data Preparation
      ↓
Train/Test Split
      ↓
TF-IDF Feature Extraction
      ↓
Logistic Regression
      ↓
Model Evaluation
      ↓
Save Trained Model
      ↓
Streamlit Web Application
      ↓
Spam / Not Spam Prediction
```

---

## Model Training

The dataset is divided into:

- **80% Training Data**
- **20% Testing Data**

The Machine Learning pipeline uses:

- TF-IDF Vectorizer
- Unigrams and bigrams
- Logistic Regression
- Balanced class weights

The trained pipeline is saved as:

```text
models/spam_email_model.pkl
```

---

## Model Performance

The model achieved the following results on the held-out test set of **611 emails**:

| Metric | Result |
|---|---:|
| Accuracy | 99.67% |
| Precision | 100% |
| Recall | 98% |
| F1-Score | 98.99% |

### Confusion Matrix

```text
[[511   0]
 [  2  98]]
```

These results describe performance on this project's held-out test dataset and should not be interpreted as a guarantee of performance on every real-world email.

---

## Application Features

The Streamlit application allows users to:

1. Paste a complete email.
2. Check whether it is Spam or Not Spam.
3. View the model's estimated probability.
4. Detect URLs in the email.
5. Detect common suspicious words.
6. View the number of email characters.
7. View model performance metrics.

---

## Project Structure

```text
Spam_Email_Detection
│
├── app.py
├── requirements.txt
├── README.md
│
├── data
│   ├── easy_ham
│   ├── spam
│   ├── 20021010_easy_ham.tar.bz2
│   ├── 20021010_spam.tar.bz2
│   └── spam_email_dataset.csv
│
├── models
│   └── spam_email_model.pkl
│
├── reports
│
├── src
│   ├── prepare_dataset.py
│   ├── train_model.py
│   └── predict.py
│
└── venv
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

---

## How to Run the Project

### Step 1: Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 2: Install Required Libraries

```powershell
python -m pip install -r requirements.txt
```

### Step 3: Run the Streamlit Application

```powershell
streamlit run app.py
```

### Step 4: Open the Application

The application will open in your browser at:

```text
http://localhost:8501
```

---

## Example: Not Spam Email

```text
Subject: Project Meeting

Hi Team,

Our project meeting is scheduled for tomorrow at 10 AM.

Please bring your latest project report.

Regards,
Lakshmi
```

Expected result:

```text
NOT SPAM
```

---

## Example: Spam Email

```text
Subject: Congratulations! You Won a Prize

Dear Customer,

Congratulations! You have won a special reward.

Click the link below to claim your prize immediately.

Regards,
Reward Team
```

Expected result:

```text
SPAM
```

---

## Email Analysis

In addition to the Machine Learning prediction, the application performs basic email analysis.

### URL Detection

The application checks whether URLs are present in the email.

### Suspicious Word Detection

The application checks for commonly suspicious terms such as:

- urgent
- winner
- prize
- claim
- free
- reward
- congratulations
- limited time
- click here
- verify

These are treated as **warning signals**, not as proof that an email is malicious.

---

## Limitations

- The model is trained on a specific public dataset.
- New types of spam emails may not always be classified correctly.
- The model's probability is an estimated model output, not a guarantee.
- URL detection and suspicious-word detection are supporting warning signals.
- A normal email may sometimes be incorrectly classified as spam.
- A spam email may sometimes be incorrectly classified as not spam.
- Real-world email filtering may require additional features such as sender reputation, email headers, domain analysis, and continuously updated datasets.

---

## Future Enhancements

- Analyze complete email headers.
- Add sender email analysis.
- Add domain analysis.
- Add URL/domain reputation checking.
- Use larger and more diverse datasets.
- Compare multiple Machine Learning algorithms.
- Add explainable AI features.
- Add real-time email filtering.
- Deploy the application online.
- Continuously update the training dataset.

---

## Conclusion

The **Spam Email Detection** project demonstrates how Machine Learning and Natural Language Processing can be applied to classify email messages.

The project combines:

- Email data preprocessing
- TF-IDF feature extraction
- Logistic Regression
- Model evaluation
- URL detection
- Suspicious-word detection
- Streamlit web application

The final application provides an easy-to-use interface for analyzing complete email messages and identifying whether they are likely to be **Spam** or **Not Spam**.

---

## Author

**Lakshmi Prasanna Ponnaganti**

**Project:** Spam Email Detection

**Domain:** Artificial Intelligence (AI)