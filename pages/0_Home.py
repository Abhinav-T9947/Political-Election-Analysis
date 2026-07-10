import streamlit as st
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Political & Election Analysis",
    page_icon="🗳️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

st.image(
    BASE_DIR / "assets" / "banner.png",
    use_container_width=True
)
st.set_page_config(
    page_title="Political & Election Analysis",
    page_icon="🗳️",
    layout="wide"
)

# --------------------------
# Header
# --------------------------

st.title("🗳️ Political & Election Analysis")

st.markdown("""
## Machine Learning Based Election Winner Prediction System

Welcome to an interactive analytics dashboard that explores historical Indian Assembly Elections
and predicts winning political parties using Machine Learning.

**Developed using:**
🐍 Python • 🤖 Scikit-Learn • 📊 Plotly • 🌐 Streamlit
""")

st.success("🎯 Deployment Model: Decision Tree Classifier | Accuracy: 98.71%")

st.divider()
# --------------------------
# Project Overview
# --------------------------

st.subheader("📌 Project Overview")

st.write("""
The objective of this project is to analyze historical election data and predict
winning political parties using Machine Learning.

The dashboard enables users to:

- 📊 Analyze election trends
- 🏛 Explore constituency-wise information
- 📈 Compare machine learning models
- 🔮 Predict winning political parties
""")

st.divider()
st.subheader("⚙️ Project Workflow")

st.markdown("""Election Dataset
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
Feature Engineering
↓
Model Training
↓
Prediction
↓
Web Deployment
""")

st.divider()
st.subheader("🤖 Machine Learning Models")

st.markdown("""
During model development, multiple machine learning algorithms were trained and evaluated.

### Models Evaluated

- 🌳 Decision Tree
- 🌲 Random Forest
- 🌳 Extra Trees

### Deployment Model

The **Decision Tree Classifier** was selected for deployment because it offers:

- ✅ Highest Accuracy (98.71%)
- ⚡ Fast Prediction Speed
- 💾 Small Model Size
- 🌐 Efficient Web Deployment using Streamlit

Although ensemble models such as Random Forest and Extra Trees were also evaluated, they require significantly larger storage and memory, making them less suitable for deployment in this web application.
""")
# --------------------------
# Dashboard Features
# --------------------------

st.subheader("🚀 Dashboard Features")

col1, col2 = st.columns(2)

with col1:

    st.success("📊 Election Analysis")

    st.write("""
- Party-wise wins
- State-wise analysis
- Election trends
- Turnout statistics
""")

    st.success("🔮 Winner Prediction")

    st.write("""
- Predict winning party
- Candidate information
- Model confidence
""")

with col2:

    st.success("📈 Model Comparison")

    st.write("""
- Decision Tree
- Random Forest
- Extra Trees
- Performance Metrics
""")

    st.success("📄 About Project")

    st.write("""
- Dataset Information
- Algorithms Used
- Methodology
- Technologies
""")

st.divider()

# --------------------------
# Technologies
# --------------------------

st.subheader("🛠 Technology Stack")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🐍 Python")
    st.success("📊 Pandas")
    st.success("🔢 NumPy")

with c2:
    st.success("🤖 Scikit-Learn")
    st.success("📈 Plotly")
    st.success("💾 Joblib")

with c3:
    st.success("🌐 Streamlit")
    st.success("📁 GitHub")
    st.success("☁️ Streamlit Cloud")

st.divider()
st.subheader("📊 Project Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Dataset Size", "32,864")
col2.metric("Models", "3")
col3.metric("Accuracy", "98.71%")
col4.metric("Deployment", "Live")

# --------------------------
# Quick Navigation
# --------------------------

st.subheader("📍 Navigate")

st.info("""
Use the **left sidebar** to explore:

🏠 Home

📊 Analysis Dashboard

🔮 Winner Prediction

📈 Model Comparison

📄 About Project
""")

st.divider()

st.caption(
    "Political & Election Analysis Dashboard | Internship Project"
)