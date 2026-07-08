import streamlit as st
st.set_page_config(
    page_title="Election Winner Prediction",
    page_icon="🗳️",
    layout="wide"
)

st.title("🗳️ Election Winner Prediction System")

st.subheader("Machine Learning Based Political Party Prediction")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Winning Constituencies", "32864")      

with col2:
    st.metric("Models Used", "3")

with col3:
    st.metric("Decision Tree Accuracy", "98.71%")   

st.markdown("---")

st.header("📌 About Project")

st.write("""
This project predicts the winning political party in an Indian Assembly Constituency using Machine Learning.

### Models Used
- Decision Tree
- Random Forest
- Extra Trees

Use the navigation menu on the left to access different sections.
""")