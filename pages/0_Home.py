import streamlit as st

st.set_page_config(
    page_title="Political & Election Analysis",
    page_icon="🗳️",
    layout="wide"
)

# --------------------------
# Header
# --------------------------

st.title("🗳️ Political & Election Analysis Dashboard")

st.markdown("""
### Machine Learning Based Election Analytics & Winner Prediction

This dashboard provides comprehensive analysis of Indian Assembly Elections
using Data Analytics and Machine Learning.
""")

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

st.subheader("🛠 Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.metric("🐍 Python", "3.x")
tech2.metric("🤖 Scikit-Learn", "ML")
tech3.metric("📊 Pandas", "Data Analysis")
tech4.metric("🎨 Streamlit", "Dashboard")

st.divider()

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