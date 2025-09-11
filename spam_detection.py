import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# load dataset
data=[]
labels=[]

with open("SMSSpamCollection", "r") as file:
    for line in file:
        parts = line.strip().split("\t",1)
        if len(parts) == 2:
            label,text=parts
            data.append(text)
            labels.append(label)

df = pd.DataFrame({'label': labels,'message': data})

print("Dataset sample: ")
print(df.head(),"\n")
print("Class distribution: \n",df["label"].value_counts(),"\n")

# split dataset

X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42) 

# convert text to numeric features

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
x_test_vec = vectorizer.transform(X_test)

# train Naive Bayes model
model=MultinomialNB()
model.fit(X_train_vec, y_train)

# evaluate model

y_pred = model.predict(x_test_vec)

print("Accuracy: ", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# example prediction
test_examples=[
    "Congratulations! You've won a $1,000 Walmart gift card. Go to http://bit.ly/123456 to claim now.",
    "Hey, are we still on for lunch tomorrow?"
]   

test_vec = vectorizer.transform(test_examples)
y_predictions = model.predict(test_vec)

print("\nCustom Predictions:")
for msg, label in zip(test_examples, y_predictions):
    print(f"Message: {msg} => Predicted Label: {label}")    
