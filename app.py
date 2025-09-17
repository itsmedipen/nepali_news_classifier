import re
import string
# from snowballstemmer import NepaliStemmer
from nltk.corpus import stopwords
import streamlit as st
import pickle

import nltk
nltk.download('stopwords')

nepali_stopwords = set(stopwords.words('nepali'))

with open("vector.pkl", "rb") as f:
    tfidf = pickle.load(f)

# Load model
with open("random_model.pkl", "rb") as f:
    model = pickle.load(f)


category_map = {
    0: "Business/Economy",
    1: "Entertainment",
    2: "National News",
    3: "Other",
    4: "Sports"
}


# Initialize once
# stemmer = NepaliStemmer()
nepali_stopwords = stopwords.words('nepali')
eng_punc = string.punctuation
nep_punct = "।॥’‘“”-—"
all_punc = eng_punc + nep_punct

def preprocess_text(text: str) -> str:
    """Full preprocessing pipeline for Nepali news text"""

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove punctuation
    for char in all_punc:
        text = text.replace(char, "")

    # Remove special characters (BOM, spaces, etc.)
    text = text.replace("\ufeff", "").replace("\ufffe", "").replace("\xfeff", "")
    text = text.replace("\r", "").replace("\n", " ")
    text = re.sub(r"\s+", " ", text).strip()

    # Remove digits (English + Nepali)
    text = re.sub(r"[0-9०-९]", "", text)

    # Remove stopwords
    words = [w for w in text.split() if w not in nepali_stopwords]

    # Apply stemming
    # words = [stemmer.stemWord(w) for w in words]

    return " ".join(words)

# Streamlit UI
st.title("Nepali News Classifier App 📰 ")

# User input
user_input = st.text_area("Enter news text in Nepali:", height=200)

if st.button("Predict",type='primary'):
    if user_input.strip() == "":
        st.warning(" Please enter some news text first.")
    else:
        # Preprocess
        cleaned = preprocess_text(user_input)
        # Transform using TF-IDF
        X_input = tfidf.transform([cleaned]).toarray()
        # Predict
        pred = model.predict(X_input)
        st.success(f"🧠Predicted Category: **{category_map[pred[0]]}**")

# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 0.9em;
        color: gray;
    }
    </style>
    <div class="footer">
        🧑Developed by <strong>Dipen Sherpa</strong>&nbsp;|&nbsp; © 2025
    </div>
    """,
    unsafe_allow_html=True
)











