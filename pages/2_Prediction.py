import streamlit as st
import joblib
from pathlib import Path
import pandas as pd

# ----------------------------
# Load Files
# ----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

dt_model = joblib.load(BASE_DIR / "dt_model.pkl")
encoders = joblib.load(BASE_DIR / "encoders.pkl")
winner_data = joblib.load(BASE_DIR / "winner_data.pkl")

# Decode encoded columns
winner_data["Constituency"] = encoders["ac_name"].inverse_transform(
    winner_data["ac_name"]
)

winner_data["Candidate"] = encoders["cand_name"].inverse_transform(
    winner_data["cand_name"]
)

winner_data["Winning Party"] = encoders["partyname"].inverse_transform(
    winner_data["partyname"]
)

winner_data["Party Abbreviation"] = encoders["partyabbre"].inverse_transform(
    winner_data["partyabbre"]
)

state_columns = [col for col in winner_data.columns if col.startswith("st_name_")]

states = [col.replace("st_name_", "") for col in state_columns]

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)

# Sidebar
with st.sidebar:

    st.title("🗳️ Election Analysis")

    st.success("Decision Tree Model")

    st.write("Model Accuracy")
    st.progress(0.987)

    st.write("Version 1.0")

    st.divider()

    st.subheader("🔮 Prediction Mode")

    prediction_mode = st.radio(
        "",
        [
            "📜 Historical Prediction",
            "🚀 Future Election Simulation"
        ]
    )

    st.divider()

    st.subheader("📥 Election Details")

    # -----------------------------
    # Select State
    # -----------------------------
    selected_state = st.selectbox(
        "📍 State",
        states
    )

    filtered = winner_data[
        winner_data[f"st_name_{selected_state}"] == True
    ]

    # =====================================================
    # HISTORICAL PREDICTION
    # =====================================================

    if prediction_mode == "📜 Historical Prediction":

        years = sorted(filtered["year"].unique())

        selected_year = st.selectbox(
            "📅 Election Year",
            years
        )

        filtered = filtered[
            filtered["year"] == selected_year
        ]

        constituencies = sorted(filtered["Constituency"].unique())

        selected_constituency = st.selectbox(
            "🏛 Constituency",
            constituencies
        )

        filtered = filtered[
            filtered["Constituency"] == selected_constituency
        ]

    # =====================================================
    # FUTURE SIMULATION
    # =====================================================

    else:

        latest_year = filtered["year"].max()

        filtered = filtered[
            filtered["year"] == latest_year
        ]

        constituencies = sorted(filtered["Constituency"].unique())

        selected_constituency = st.selectbox(
            "🏛 Constituency",
            constituencies
        )

        filtered = filtered[
            filtered["Constituency"] == selected_constituency
        ]

        future_year = st.number_input(
            "📅 Future Election Year",
            min_value=int(latest_year + 1),
            value=int(latest_year + 5),
            step=1
        )
# Main Title
st.title("🗳️ Political & Election Analysis")

st.caption("Machine Learning Based Election Winner Prediction Dashboard")

st.markdown("---")


filtered = filtered[
    filtered["Constituency"] == selected_constituency
]

record = filtered.iloc[0]

st.markdown("---")

st.markdown("---")
# Determine AC Type
if record["ac_type_GEN"]:
    ac_type = "GEN"
elif record["ac_type_SC"]:
    ac_type = "SC"
elif record["ac_type_ST"]:
    ac_type = "ST"
elif record["ac_type_BL"]:
    ac_type = "BL"
else:
    ac_type = "SANGH"
st.subheader("📋 Selected Election Details")

c1, c2, c3 = st.columns(3)

c1.metric("📍 State", selected_state)

if prediction_mode == "📜 Historical Prediction":

    c2.metric(
        "📅 Election Year",
        int(selected_year)
    )

else:

    c2.metric(
        "🚀 Simulated Year",
        int(future_year)
    )

c3.metric(
    "🏛 Constituency",
    record["Constituency"]
)
c4, c5 = st.columns(2)

c4.metric(
    "👥 Electors",
    f"{int(record['electors']):,}"
)

c5.metric(
    "🏷️ AC Type",
    ac_type
)

st.divider()

st.markdown("---")
st.info("""
### 🤖 Deployment Model

This web application uses the **Decision Tree Classifier** for prediction.

Why?

• Highest Accuracy: **98.71%**

• Fast prediction

• Lightweight model

• Suitable for real-time deployment

Other models (Random Forest and Extra Trees) were evaluated during development but were not deployed due to their significantly larger model sizes.
""")
# ----------------------------
# Prediction
# ----------------------------
if st.button("🔮 Predict Winning Party"):

    # Create a copy of the selected record
    simulation_record = record.copy()

    # Use future year if simulation mode
    if prediction_mode == "🚀 Future Election Simulation":
        simulation_record["year"] = future_year

    # Model input
    X = simulation_record[dt_model.feature_names_in_]
    X = pd.DataFrame([X])

    # Predict
    probabilities = dt_model.predict_proba(X)[0]
    classes = dt_model.classes_

    top3_idx = probabilities.argsort()[-3:][::-1]
    top3_classes = classes[top3_idx]
    top3_probabilities = probabilities[top3_idx] * 100

    prediction = encoders["partyname"].inverse_transform(
        [top3_classes[0]]
    )[0]

    probability = top3_probabilities[0]

    actual = record["Winning Party"]

    st.success("✅ Prediction Completed!")

    st.subheader("🏆 Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("👤 Winning Candidate")
        st.markdown(f"### {record['Candidate']}")

    with col2:
        st.success("🏛 Predicted Party")
        st.markdown(f"### {prediction}")

    if prediction_mode == "📜 Historical Prediction":

        with col3:
            st.warning("📋 Actual Party")
            st.markdown(f"### {actual}")

    else:

        with col3:
            st.info("🚀 Simulation")
            st.markdown("### Future Prediction")

    st.metric(
        "🎯 Prediction Confidence",
        f"{probability:.2f}%"
    )

    if prediction_mode == "📜 Historical Prediction":

        if prediction == actual:
            st.balloons()
            st.success("🎉 Model Prediction is Correct!")
        else:
            st.error("⚠️ Model Prediction does not match the actual winner.")

    else:
        st.info(
            "🚀 This is a simulated prediction for a future election. "
            "No actual result exists yet for comparison."
        )