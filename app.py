import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from model import get_model, predict_career, load_data

# Page Setup
st.set_page_config(page_title="Career Navigator AI", layout="wide")

# Load model and data
@st.cache_resource
def init_app():
    return get_model()

model, le, acc = init_app()
df = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Predictor", "Analytics Dashboard"])

# --- PAGE 1: PREDICTOR ---
if page == "Predictor":
    st.title("🎯 Career Recommendation Engine")
    st.write("Enter your profile details in the sidebar to generate a match.")
    
    with st.sidebar:
        st.divider()
        st.subheader("User Profile")
        math = st.slider("Math Score", 0, 100, 75)
        sci = st.slider("Science Score", 0, 100, 70)
        eng = st.slider("English Score", 0, 100, 80)
        
        st.subheader("Skills (1-10)")
        coding = st.number_input("Coding", 1, 10, 5)
        comm = st.number_input("Communication", 1, 10, 5)
        creat = st.number_input("Creativity", 1, 10, 5)
        
        st.subheader("Interests")
        tech = st.checkbox("Technology", True)
        arts = st.checkbox("Arts")
        biz = st.checkbox("Business")

    if st.button("Generate Recommendation", type="primary"):
        user_data = {
            "math_score": math, "science_score": sci, "english_score": eng,
            "coding_skill": coding, "communication_skill": comm, "creativity_skill": creat,
            "interest_technology": int(tech), "interest_arts": int(arts),
            "interest_business": int(biz), "interest_medicine": 0, "interest_law": 0
        }
        
        results = predict_career(model, le, user_data)
        
        st.markdown("### Your Top Matches")
        cols = st.columns(3)
        for i, res in enumerate(results):
            with cols[i]:
                st.info(f"**{res['icon']} {res['career']}**")
                st.metric("Match Confidence", f"{res['confidence']}%")
                st.write(res['desc'])

# --- PAGE 2: ANALYTICS ---
else:
    st.title("📊 Data & Measuring Graphics")
    st.write("Explore the dataset trends and model performance metrics.")
    
    # Row 1: Key Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Model Accuracy", f"{acc*100:.1f}%")
    m2.metric("Total Records", len(df))
    m3.metric("Career Categories", df['career_label'].nunique())

    st.divider()

    # Row 2: Visualizations
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("📈 Career Distribution")
        fig, ax = plt.subplots()
        sns.countplot(data=df, x='career_label', palette='viridis', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col_right:
        st.subheader("⚖️ Skills Comparison")
        # Native Streamlit bar chart for comparing averages
        avg_skills = df.groupby('career_label')[['coding_skill', 'creativity_skill']].mean()
        st.bar_chart(avg_skills)

    st.subheader("🔍 Correlation Heatmap")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_df.corr(), annot=True, cmap='RdBu', ax=ax2)
    st.pyplot(fig2)