# 🚗 Accident Severity Prediction

An end-to-end machine learning project that predicts accident severity using weather, location, time, and road-related features.

## Features

- Exploratory Data Analysis using Pandas, Matplotlib and Seaborn
- Multiclass accident severity classification using Random Forest
- Model evaluation using Accuracy, Balanced Accuracy and Macro F1
- Interactive Streamlit web application for real-time prediction

## Model Performance

- Accuracy: 78.5%
- Balanced Accuracy: 39.2%
- Macro F1: 39.2%

> Balanced Accuracy and Macro F1 are reported because the accident severity classes are highly imbalanced.

## Tech Stack

Python, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit, Joblib

## Project Structure

- `01_data_exploration.ipynb` — Data cleaning and EDA
- `02_machine_learning.ipynb` — Model training and evaluation
- `app.py` — Streamlit prediction application
- `requirements.txt` — Python dependencies
