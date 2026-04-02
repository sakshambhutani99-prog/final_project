import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

FEATURES = [
    "math_score", "science_score", "english_score",
    "coding_skill", "communication_skill", "creativity_skill",
    "interest_technology", "interest_arts", "interest_business",
    "interest_medicine", "interest_law"
]

def load_data():
    # Make sure 'data/students.csv' exists in your folder!
    return pd.read_csv("data/students.csv")

def get_model():
    df = load_data()
    le = LabelEncoder()
    y = le.fit_transform(df["career_label"])
    X = df[FEATURES]
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    acc = model.score(X, y)
    return model, le, acc

def predict_career(model, le, input_dict):
    input_df = pd.DataFrame([input_dict])[FEATURES]
    probs = model.predict_proba(input_df)[0]
    top_indices = np.argsort(probs)[-3:][::-1]
    
    icons = {"Software Engineer": "💻", "Doctor": "🩺", "Lawyer": "⚖️", "Data Scientist": "📊", "Graphic Designer": "🎨"}
    
    results = []
    for i in top_indices:
        name = le.inverse_transform([i])[0]
        results.append({
            "career": name,
            "confidence": int(probs[i] * 100),
            "icon": icons.get(name, "🌟"),
            "desc": "A strong match based on your aptitude and interests."
        })
    return results