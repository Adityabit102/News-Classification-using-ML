import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load the merged Kaggle dataset
df = pd.read_csv("news_kaggle_merged.csv")
df['label'] = df['label'].map({'FAKE': 0, 'REAL': 1})

# Prepare the training data
X = df['text']
y = df['label']

# Vectorize the text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# Train the classifier
model = LogisticRegression()
model.fit(X_vec, y)

# Streamlit UI
st.set_page_config(page_title="News Classifier", page_icon="📰")
st.title("📰 Fake News Detector")
st.write("Enter a news article or headline below to check if it's likely **FAKE** or **REAL**.")

# User input
user_input = st.text_area("📝 Your News Text", height=200)

# Prediction button
if st.button("🔍 Classify"):
    if not user_input.strip():
        st.warning("⚠️ Please enter some text before clicking classify.")
    else:
        input_vec = vectorizer.transform([user_input])
        prediction = model.predict(input_vec)[0]
        label = "✅ REAL" if prediction == 1 else "❌ FAKE"
        st.success(f"**Prediction:** {label}")
