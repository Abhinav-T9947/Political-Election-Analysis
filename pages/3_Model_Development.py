#🤖 Model Development
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Model Development",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Machine Learning Model Development")

st.write(
    """
Several machine learning algorithms were trained and evaluated to identify the
best model for predicting the winning political party.
"""
)
#Model Comparison Table
comparison = pd.DataFrame({

    "Model":[
        "Decision Tree",
        "Random Forest",
        "Extra Trees"
    ],

    "Accuracy":[
        "98.71%",
        "95.xx%",
        "86.xx%"
    ],

    "Deployment":[
        "✅ Selected",
        "❌ Not Deployed",
        "❌ Not Deployed"
    ],

    "Reason":[
        "Highest accuracy, lightweight, fast",
        "Large model size",
        "Very large model size"
    ]
})

st.dataframe(
    comparison,
    use_container_width=True
)
#Why Decision Tree?
st.subheader("🏆 Why Decision Tree?")

st.success("""
The Decision Tree Classifier was selected for deployment because it provides
the best balance between accuracy, prediction speed and memory usage.

Although Random Forest and Extra Trees are powerful ensemble algorithms,
their model files were significantly larger, making them less suitable for
deployment in a lightweight Streamlit web application.
""")
import plotly.express as px

accuracy = pd.DataFrame({

    "Model":[
        "Decision Tree",
        "Random Forest",
        "Extra Trees"
    ],

    "Accuracy":[
        98.71,
        93.74,
        85.7
    ]

})

fig = px.bar(
    accuracy,
    x="Model",
    y="Accuracy",
    color="Accuracy",
    title="Model Accuracy Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
#Deployment summary
st.subheader("🚀 Deployment Summary")

st.markdown("""
### Development Phase

✔ Decision Tree trained

✔ Random Forest trained

✔ Extra Trees trained

✔ Model evaluation completed

---

### Deployment Phase

Only the **Decision Tree Classifier** was deployed because it offers:

- Highest prediction accuracy
- Fast inference
- Small model size
- Better memory efficiency
- Suitable for real-time prediction
""")
import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Model Development",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# HEADER
# =====================================================

st.title("🤖 Machine Learning Model Development")

st.caption(
    "Model training, evaluation and deployment process followed for the Election Prediction System."
)

st.divider()

# =====================================================
# WORKFLOW
# =====================================================

st.subheader("🛠 Machine Learning Workflow")

st.markdown("""Dataset
↓
Data Cleaning
↓
Feature Engineering
↓
Model Training
↓
Model Evaluation
↓
Model Selection
↓
Deployment""")

st.divider()

# =====================================================
# MODEL COMPARISON
# =====================================================

st.subheader("📊 Model Comparison")

comparison = pd.DataFrame({

    "Model":[
        "Decision Tree",
        "Random Forest",
        "Extra Trees"
    ],

    "Accuracy":[
        98.71,
        95.00,
        86.00
    ],

    "Deployment":[
        "✅ Selected",
        "❌ Not Deployed",
        "❌ Not Deployed"
    ],

    "Reason":[
        "Highest Accuracy + Lightweight",
        "Large Model Size",
        "Very Large Model Size"
    ]

})

st.dataframe(
    comparison,
    use_container_width=True
)

st.divider()

# =====================================================
# ACCURACY CHART
# =====================================================

fig = px.bar(
    comparison,
    x="Model",
    y="Accuracy",
    color="Accuracy",
    text="Accuracy",
    title="Model Accuracy Comparison",
    template="plotly_white"
)

fig.update_layout(
    title_x=0.5,
    coloraxis_showscale=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =====================================================
# MODEL CHARACTERISTICS
# =====================================================

st.subheader("⚖ Model Characteristics")

characteristics = pd.DataFrame({

    "Feature":[
        "Accuracy",
        "Prediction Speed",
        "Memory Usage",
        "Model Size",
        "Deployment"
    ],

    "Decision Tree":[
        "⭐⭐⭐⭐⭐",
        "⭐⭐⭐⭐⭐",
        "⭐⭐⭐⭐⭐",
        "⭐⭐⭐⭐⭐",
        "✅"
    ],

    "Random Forest":[
        "⭐⭐⭐⭐",
        "⭐⭐⭐",
        "⭐⭐",
        "⭐⭐",
        "❌"
    ],

    "Extra Trees":[
        "⭐⭐⭐",
        "⭐⭐⭐",
        "⭐",
        "⭐",
        "❌"
    ]

})

st.dataframe(
    characteristics,
    use_container_width=True
)

st.divider()

# =====================================================
# WHY DECISION TREE
# =====================================================

st.subheader("🏆 Why Decision Tree?")

st.success("""
The Decision Tree Classifier was selected as the deployment model because it
provides the best balance between prediction accuracy, execution speed and
deployment efficiency.

### Advantages

✅ Highest Accuracy (98.71%)

✅ Fast Prediction

✅ Small Model Size

✅ Low Memory Consumption

✅ Suitable for Real-Time Web Deployment
""")

st.divider()

# =====================================================
# DEPLOYMENT DECISION
# =====================================================

st.subheader("🚀 Deployment Decision")

st.info("""
During model development, three machine learning algorithms were trained and evaluated.

• Decision Tree

• Random Forest

• Extra Trees

Although Random Forest and Extra Trees achieved competitive performance,
their serialized model sizes were significantly larger, requiring considerably
more memory during deployment.

The Decision Tree model achieved the highest prediction accuracy while
remaining lightweight and computationally efficient.

Therefore, the Decision Tree Classifier was selected as the production model
for deployment in the Streamlit web application.
""")

st.divider()

# =====================================================
# FINAL SUMMARY
# =====================================================

st.subheader("📌 Summary")

st.markdown("""
### ✔ Development Completed

- Data Cleaning
- Feature Engineering
- Model Training
- Model Evaluation
- Model Comparison
- Model Selection
- Web Deployment

---

### ✔ Final Deployment Model

**Decision Tree Classifier**

**Accuracy : 98.71%**

Selected because it provides the best combination of:

- Prediction Accuracy
- Execution Speed
- Lightweight Deployment
- Low Memory Usage
""")

st.divider()

st.markdown(
"""
---
<center>

### 🤖 Machine Learning Development Report

Political & Election Analysis Dashboard

Developed using

**Python • Scikit-Learn • Streamlit • Plotly**

</center>
""",
unsafe_allow_html=True
)