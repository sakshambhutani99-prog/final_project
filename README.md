# 🎓 AI-Powered Smart Career Recommendation System
**TalentGro Global | BTech 4th Semester | Python Programming**

---

## 📁 Project Structure
```
career_recommender/
├── app.py              ← Main Streamlit web app
├── model.py            ← ML model (Random Forest)
├── requirements.txt    ← Python dependencies
├── README.md           ← This file
└── data/
    └── students.csv    ← Student dataset (40 records)
```

---

## 🚀 How to Run

### Step 1 — Install Python
Make sure Python 3.9+ is installed on your system.

### Step 2 — Install dependencies
Open terminal in the project folder and run:
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 🧠 How It Works

1. **Input**: Student enters math, science, English scores, skill ratings (1–10), and interests
2. **Processing**: Data is fed into a trained Random Forest classifier
3. **Output**: Top 3 career matches with confidence scores and skill recommendations

---

## 🛠️ Technology Stack

| Layer         | Technology             |
|---------------|------------------------|
| Backend       | Python + Scikit-learn  |
| Frontend/UI   | Streamlit              |
| ML Model      | Random Forest Classifier|
| Data Handling | Pandas, NumPy          |
| Visualization | Matplotlib, Seaborn    |

---

## 📊 Features

- ✅ Interactive input sliders and checkboxes
- ✅ Top 3 career recommendations with confidence %
- ✅ Feature importance chart
- ✅ Career distribution pie chart
- ✅ Score heatmap by career
- ✅ Dataset explorer with search & CSV download
- ✅ Model accuracy display

---

## 🎯 Career Paths Covered

- 💻 Software Engineer
- 📊 Data Scientist
- 🤖 AI/ML Engineer
- 🩺 Doctor
- ⚖️ Lawyer
- 📈 Business Manager
- 📣 Marketing Executive
- 🎨 Graphic Designer
- ✍️ Content Creator

---

## 👥 Target Users
- Students (Class X–XII and College)
- Career Counselors
- Educational Institutions
