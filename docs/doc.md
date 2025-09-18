# 📰 Nepali News Classifier App

This is a **Streamlit-based web application** that classifies Nepali news articles into categories using a trained machine learning model (TF-IDF + Random Forest).

## 🚀 Features
- Cleans and preprocesses Nepali text (removes stopwords, punctuation, digits, URLs, HTML tags).
- Converts text into vectors using **TF-IDF**.
- Predicts news category with a trained **Random Forest** model.
- Simple, interactive UI with **Streamlit**.
- Supports 5 categories:
  - 0 → Business/Economy  
  - 1 → Entertainment  
  - 2 → National News  
  - 3 → Other  
  - 4 → Sports  

## 🛠️ Requirements
Install dependencies:
```bash
pip install streamlit scikit-learn nltk

📂 Files

app.py → Streamlit app

vector.pkl → Saved TF-IDF vectorizer

random_model.pkl → Trained ML model

▶️ Run the App

streamlit run app.py

Then open: http://localhost:8501

🧠 Model Info

Vectorizer: TF-IDF with n-grams

Model: Random Forest Classifier

Training Data: ~12,198 Nepali news articles

Test Accuracy: ~92.88%

👨‍💻 Author

Developed by Dipen Sherpa | © 2025