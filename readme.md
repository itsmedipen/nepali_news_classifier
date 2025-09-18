# 📰 Nepali News Classifier with TF-IDF, Random Forest & Streamlit

This project builds a web application that can classify Nepali news articles into predefined categories.  
It uses **TF-IDF** for text vectorization, a **Random Forest** model for classification, and **Streamlit** for a user-friendly interface.

---

## ✨ Features
- **Text Preprocessing**: Cleans input (removes stopwords, punctuation, digits, URLs, and HTML tags).  
- **TF-IDF Vectorization**: Converts Nepali text into numerical vectors.  
- **Classification**: Predicts the news category using a trained Random Forest model.  
- **Streamlit UI**: Simple and interactive web interface for prediction.  
- **Supported Categories**:
  - 0 → Business/Economy  
  - 1 → Entertainment  
  - 2 → National News  
  - 3 → Other  
  - 4 → Sports  

---

## ⚙️ How It Works
### Text Processing
1. The input Nepali news article is cleaned (stopwords, punctuation, and numbers removed).  
2. The cleaned text is transformed into vectors using the trained **TF-IDF vectorizer**.  

### Model Prediction
1. The vectorized text is fed into the **Random Forest Classifier**.  
2. The model outputs the most likely category for the article.  
3. The predicted category is displayed in the **Streamlit app**.  

---

## 🛠️ Installation
### Clone the Repository:
```bash
git clone https://github.com/itsmedipen/nepali_news_classifier.git
cd nepali_news_classifier

Create & Activate a Virtual Environment:

cmd

conda create -p venv python==3.12 -y
source venv/bin/activate    # On Windows use `venv\Scripts\activate`

Install Dependencies:

pip install -r requirements.txt

▶️ Running the Application

streamlit run app.py

Using the app:

Enter a Nepali news article in the text box.
Click Predict.
The app will show the predicted category.


📂 File Structure

nepali_news_classifier/
├── app.py                     # Streamlit app
├── nepali_news_classifier.ipynb  # Jupyter notebook (exploration/training)
├── models/
│   ├── random_model.pkl       # Trained Random Forest model
│   └── vector.pkl             # Saved TF-IDF vectorizer
├── docs/
│   ├── doc.md                 # Technical documentation
│   └── Final_Documentation.docx # details explanation of the project
├── requirements.txt           # Dependencies
├── README.md                  # Project overview
├── .gitignore
└── venv/                      # (local virtual env – should be ignored)



🔐 Security & Best Practices

Keep large model/vectorizer files (.pkl) out of Git when possible, or use Git LFS.
Use a .gitignore to exclude unnecessary files (venv/, __pycache__/, etc.).

🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

📜 License

This project is licensed under the MIT License.

