
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

def train_and_save_model():
    # Load dataset
    data, labels = [], []
    with open("SMSSpamCollection", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split('\t', 1)
            if len(parts) == 2:
                label, text = parts
                data.append(text)
                labels.append(label)

    df = pd.DataFrame({'label': labels, 'message': data})

    # Train model
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['message'])
    y = df['label']

    model = MultinomialNB()
    model.fit(X, y)

    # Save model + vectorizer
    joblib.dump(model, "spam_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

if __name__ == "__main__":
    train_and_save_model()
