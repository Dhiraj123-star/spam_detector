from fastapi import FastAPI
from pydantic import BaseModel
import joblib


# load trained model & vectorizer

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = FastAPI(
    title="Spam Detection API",
    description="Classify SMS messages as spam or ham",
    version="1.0.0",
)

# input schema
class Message(BaseModel):
    text: str

@app.post("/predict")
def predict_spam(message: Message):
    vectorized_message = vectorizer.transform([message.text])
    prediction = model.predict(vectorized_message)[0]
    return {"message":message.text,"prediction": prediction}