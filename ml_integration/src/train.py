import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import os

def train_model(csv_path: str, model_save_path: str):
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Data file not found at {csv_path}")

    df = pd.read_csv(csv_path)
    
    # create Pipeline
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    
    # train
    model.fit(df['task_description'], df['priority'])
    
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    
    # save
    joblib.dump(model, model_save_path)
    print(f"Model trained and saved to {model_save_path}")

if __name__ == "__main__":
    train_model("data/tasks.csv", "models/model.pkl")