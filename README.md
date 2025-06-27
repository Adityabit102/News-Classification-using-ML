📰 Fake News Detection Using Machine Learning

** Due to size restrictions I am unable to upload the Datasets **
Download Here- 
https://drive.google.com/file/d/1TOa0daB_ywM2lOMeGrlInOZFOjJmhx_V/view?usp=share_link  (True.csv)
https://drive.google.com/file/d/1_pjs6dSlS-D-SfhWf8lR883xCk4-avig/view?usp=share_link  (Fake.csv)
https://drive.google.com/file/d/12aeNtzijQG-Y7w2SftonV5lYkLgfIO3w/view?usp=share_link  (merged)

This project is a machine learning-powered system that classifies news articles as FAKE or REAL based on their content. It uses natural language processing (NLP) and a Logistic Regression model, and provides a user-friendly web interface built with Streamlit.

📌 Project Objective
To identify whether a given news article is real or fake using text classification techniques and provide predictions through an interactive web app.

📂 Dataset
Source: Kaggle – Fake and Real News Dataset
Files used:
Fake.csv
True.csv
These were merged and labeled to form news_kaggle_merged.csv.

🛠 Tools & Technologies
Python 3
pandas
scikit-learn
Streamlit
Jupyter Notebook
TfidfVectorizer
Logistic Regression

🚀 How to Run the Project
1. Clone the Repository

git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
2. Install Dependencies

pip install -r requirements.txt
3. Run the Jupyter Notebook

Open the notebook to explore the training and evaluation steps:

jupyter notebook news_kaggle_classifier.ipynb
4. Launch the Streamlit App

Make sure news_kaggle_merged.csv is in the same directory as app.py, then run:

streamlit run app.py

📷 Screenshot
<img width="1219" alt="Screenshot 2025-06-27 at 1 45 48 PM" src="https://github.com/user-attachments/assets/eb1820c7-bce5-4116-8100-77c131635095" />


📝 Output
The model predicts FAKE ❌ or REAL ✅ for any given news content.
Includes metrics such as accuracy, precision, recall, and F1-score in the notebook.

📄 Files in This Repository
File	Description
Fake.csv, True.csv	Original datasets from Kaggle
news_kaggle_merged.csv	Merged and labeled dataset
news_kaggle_classifier.ipynb	Jupyter notebook with full ML pipeline
app.py	Streamlit web application
requirements.txt	List of Python packages used
README.md
project report

🙌 Acknowledgements
Dataset by Clement Bisaillon on Kaggle.
Inspired by real-world challenges of misinformation detection.
