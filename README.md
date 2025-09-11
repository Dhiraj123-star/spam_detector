

# 📧 Spam Detector

A simple **spam detection application** that classifies SMS messages as **spam** (unwanted) or **ham** (genuine).

---

## 🚀 Features

* Uses a **Naive Bayes model** for text classification
* Trained on the **SMS Spam Collection dataset** (UCI ML Repository)
* Achieves high accuracy (\~97%)
* Provides predictions for custom input messages

---

## 📂 Dataset

* Source: [SMS Spam Collection Dataset – UCI ML Repository](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection)
* Contains 5,574 SMS messages labeled as **ham** or **spam**

---

## ⚙️ Workflow

1. Load and preprocess dataset
2. Split into training and testing sets
3. Convert text messages into numerical features
4. Train a **Naive Bayes classifier**
5. Evaluate accuracy and generate predictions

---

## ▶️ Example Output

* Accuracy score on test data (\~97%)
* Predictions for custom messages:

  * `"Congratulations! You've won a $1,000 Walmart gift card."` → **spam**
  * `"Hey, are we still on for lunch tomorrow?"` → **ham**

---

## 📌 Future Enhancements

* Save and reuse trained model
* Create a command-line interface (CLI) for instant predictions
* Wrap into a REST API for real-time use

---
