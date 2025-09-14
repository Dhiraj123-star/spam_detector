
# 📧 Spam Detector API

A simple **spam detection application** that classifies SMS messages as **spam** (unwanted) or **ham** (genuine), powered by **FastAPI**.

---

## 🚀 Features

* **Naive Bayes model** trained on the SMS Spam Collection dataset
* REST API built with **FastAPI** and interactive Swagger UI
* Containerized with **Docker** and ready-to-run using **Docker Compose**
* Integrated **CI/CD pipelines with GitHub Actions** for automated build, test, and deployment
* Predicts whether an input message is **spam** or **ham**

---

## 📂 Dataset

* Source: [SMS Spam Collection Dataset – UCI ML Repository](https://archive.ics.uci.edu/dataset/228/sms%2Bspam%2Bcollection)
* 5,574 SMS messages labeled as **ham** or **spam**

---

## ⚙️ Workflow

1. Load and preprocess dataset
2. Train a **Naive Bayes classifier**
3. Serve predictions through a **FastAPI endpoint**
4. Access via Swagger UI at `http://localhost:8000/docs`
5. Automate build, test, and deploy with **CI/CD pipelines**

---

## ▶️ Example Usage

* Run with Docker Compose:

  ```bash
  docker-compose up --build
  ```

* Open Swagger UI:

  ```
  http://localhost:8000/docs
  ```

* Test a message:

  * `"Congratulations! You've won a $1,000 Walmart gift card."` → **spam**
  * `"Hey, are we still on for lunch tomorrow?"` → **ham**

---

## ⚡ CI/CD Pipelines

* Built with **GitHub Actions**
* Automatically triggered on each push or pull request
* Workflow steps: **install dependencies → run tests → build Docker image → push to registry → deploy**

---
