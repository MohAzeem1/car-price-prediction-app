# 🚗 Car Price Prediction App

A Machine Learning web application that predicts the price of used cars based on various features like year, mileage, engine, fuel type, and more.

---

## 📌 Project Overview

This project implements an end-to-end Machine Learning pipeline to predict used car prices.
The application is deployed using **Streamlit**, allowing users to interactively input car details and get predictions instantly.

---

## 🚀 Live Demo

👉 https://moh-azeem-car-cost-prediction.streamlit.app

---

## 🛠️ Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn
* Matplotlib & Seaborn
* Streamlit
* Joblib

---

## 📊 Features

* ✅ Real-time car price prediction
* ✅ Confidence score using Random Forest
* ✅ Interactive UI with multiple inputs
* ✅ Data analytics dashboard
* ✅ Feature importance visualization
* ✅ Deployed on Streamlit Cloud

---

## 📁 Project Structure

```
car-price-prediction-app/
│
├── app.py
├── car_price_model.pkl
├── columns.pkl
├── car_price_prediction.csv
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## 🧠 Model Comparison

| Model             | R² Score | Observation                                         |
| ----------------- | -------- | --------------------------------------------------- |
| Linear Regression | ~0.75    | Underfitting, unable to capture non-linear patterns |
| Random Forest     | ~0.89    | Better performance, captures complex relationships  |

👉 Final model selected: **Random Forest Regressor**

---

## 🔁 Cross Validation

Cross-validation was used to ensure model stability and avoid overfitting.

* CV Score (R²): ~0.88
* Indicates consistent performance across different data splits

---

## 📊 Exploratory Data Analysis (EDA) Insights

* 📉 **Kilometers Driven vs Price**: Negative correlation
  → More usage → Lower price

* 📈 **Year vs Price**: Positive correlation
  → Newer cars → Higher price

* ⛽ **Fuel Type Impact**: Diesel cars tend to have higher resale value

* ⚙️ **Engine & Power**: Higher engine capacity and power generally increase price

* 🚗 **Mileage**: Moderate impact, varies across car segments

---

## ⚙️ Model Details

* Model: Random Forest Regressor
* Evaluation Metrics:

  * R² Score ≈ 0.89
  * MAE ≈ 50,000
* Confidence score derived using variance across trees

---

## 📈 Dataset Features

* Year
* Kilometers Driven
* Fuel Type
* Transmission
* Engine (CC)
* Mileage (km/l)
* Seats
* Selling Price

---

## 💡 Key Learnings

* Built a complete ML pipeline from EDA to deployment
* Compared multiple models and selected the best performer
* Used cross-validation for reliable evaluation
* Handled feature mismatch between training and deployment
* Deployed ML model as a web application

---

## 🔮 Future Improvements

* Add batch prediction using CSV upload
* Improve UI/UX with animations
* Add model comparison dashboard inside app
* Deploy using Docker / AWS
* Integrate real-time data

---

## 👨‍💻 Author

**Moh Azeem**

🔗 GitHub: https://github.com/MohAzeem1

---

## 📜 License

This project is open-source and available for learning purposes.
