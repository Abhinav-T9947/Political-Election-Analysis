import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Political & Election Analysis",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

winner_data = joblib.load(BASE_DIR / "winner_data.pkl")
encoders = joblib.load(BASE_DIR / "encoders.pkl")

# =====================================================
# DECODE COLUMNS
# =====================================================

winner_data["Constituency"] = encoders["ac_name"].inverse_transform(
    winner_data["ac_name"]
)

winner_data["Winning Party"] = encoders["partyname"].inverse_transform(
    winner_data["partyname"]
)

winner_data["Party"] = encoders["partyabbre"].inverse_transform(
    winner_data["partyabbre"]
)

winner_data["Candidate"] = encoders["cand_name"].inverse_transform(
    winner_data["cand_name"]
)

# =====================================================
# RECOVER STATE NAME
# =====================================================

state_columns = [
    c for c in winner_data.columns
    if c.startswith("st_name_")
]

winner_data["State"] = (
    winner_data[state_columns]
    .idxmax(axis=1)
    .str.replace("st_name_", "")
)

# =====================================================
# DASHBOARD HEADER
# =====================================================

st.title("📊 Political & Election Analysis Dashboard")

st.caption(
    "Interactive Dashboard for Historical Election Analysis and Machine Learning Insights"
)

# =====================================================
# SIDEBAR FILTERS
# =====================================================

st.sidebar.header("🎛 Dashboard Filters")

filtered = winner_data.copy()

# State Filter
selected_state = st.sidebar.selectbox(
    "📍 Select State",
    ["All States"] + sorted(winner_data["State"].unique())
)

if selected_state != "All States":
    filtered = filtered[
        filtered["State"] == selected_state
    ]

# Year Filter
years = sorted(filtered["year"].unique())

selected_year = st.sidebar.selectbox(
    "📅 Select Election Year",
    ["All Years"] + years
)

if selected_year != "All Years":
    filtered = filtered[
        filtered["year"] == selected_year
    ]

# Party Filter
parties = sorted(filtered["Winning Party"].unique())

selected_party = st.sidebar.selectbox(
    "🏆 Select Political Party",
    ["All Parties"] + parties
)

if selected_party != "All Parties":
    filtered = filtered[
        filtered["Winning Party"] == selected_party
    ]

st.divider()

# =====================================================
# KPI CARDS
# =====================================================

total_years = filtered["year"].nunique()

total_states = filtered["State"].nunique()

total_constituencies = filtered["Constituency"].nunique()

total_parties = filtered["Winning Party"].nunique()

total_candidates = filtered["Candidate"].nunique()

total_votes = int(filtered["totvotpoll"].sum())

k1, k2, k3 = st.columns(3)

k4, k5, k6 = st.columns(3)

k1.metric(
    "🗳 Elections",
    total_years
)

k2.metric(
    "🗺 States",
    total_states
)

k3.metric(
    "🏛 Constituencies",
    total_constituencies
)

k4.metric(
    "🏆 Parties",
    total_parties
)

k5.metric(
    "👤 Candidates",
    total_candidates
)

k6.metric(
    "🗳 Total Votes",
    f"{total_votes:,}"
)

st.divider()
# =====================================================
# CHART DATA
# =====================================================

party_wins = (
    filtered["Winning Party"]
    .value_counts()
    .head(10)
    .reset_index()
)

party_wins.columns = ["Party", "Wins"]


trend = (
    filtered
    .groupby("year")
    .size()
    .reset_index(name="Constituencies")
)


top_candidates = (
    filtered["Candidate"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_candidates.columns = ["Candidate", "Wins"]


top_constituencies = (
    filtered["Constituency"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_constituencies.columns = ["Constituency", "Elections"]


elector_stats = (
    filtered
    .groupby("year")["electors"]
    .mean()
    .reset_index()
)

# =====================================================
# CHARTS
# =====================================================

fig_party = px.bar(
    party_wins,
    x="Wins",
    y="Party",
    orientation="h",
    color="Wins",
    title="🏆 Top Political Parties by Election Wins",
    template="plotly_white"
)

fig_party.update_layout(
    title_x=0.5,
    coloraxis_showscale=False
)

fig_pie = px.pie(
    party_wins,
    names="Party",
    values="Wins",
    title="🥧 Party-wise Win Share",
    template="plotly_white"
)

fig_pie.update_layout(
    title_x=0.5
)

fig_trend = px.line(
    trend,
    x="year",
    y="Constituencies",
    markers=True,
    title="📈 Election Trend",
    template="plotly_white"
)

fig_trend.update_layout(
    title_x=0.5
)

fig_candidate = px.bar(
    top_candidates,
    x="Wins",
    y="Candidate",
    orientation="h",
    color="Wins",
    title="👤 Top Winning Candidates",
    template="plotly_white"
)

fig_candidate.update_layout(
    title_x=0.5,
    coloraxis_showscale=False
)

fig_constituency = px.bar(
    top_constituencies,
    x="Elections",
    y="Constituency",
    orientation="h",
    color="Elections",
    title="🏛 Most Active Constituencies",
    template="plotly_white"
)

fig_constituency.update_layout(
    title_x=0.5,
    coloraxis_showscale=False
)

fig_electors = px.line(
    elector_stats,
    x="year",
    y="electors",
    markers=True,
    title="👥 Average Electors Across Elections",
    template="plotly_white"
)

fig_electors.update_layout(
    title_x=0.5
)

# =====================================================
# ROW 1
# =====================================================

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_party,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

st.divider()

# =====================================================
# ROW 2
# =====================================================

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_candidate,
        use_container_width=True
    )

st.divider()

# =====================================================
# ROW 3
# =====================================================

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_constituency,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_electors,
        use_container_width=True
    )

st.divider()
# =====================================================
# DASHBOARD HIGHLIGHTS
# =====================================================

st.subheader("⭐ Dashboard Highlights")

top_party = filtered["Winning Party"].value_counts().idxmax()
top_party_wins = filtered["Winning Party"].value_counts().max()

top_candidate = filtered["Candidate"].value_counts().idxmax()
top_candidate_wins = filtered["Candidate"].value_counts().max()

top_state = filtered["State"].value_counts().idxmax()
top_state_count = filtered["State"].value_counts().max()

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🏆 Most Successful Party")
    st.markdown(f"### {top_party}")
    st.caption(f"Election Wins : {top_party_wins}")

with c2:
    st.info("👤 Top Winning Candidate")
    st.markdown(f"### {top_candidate}")
    st.caption(f"Election Wins : {top_candidate_wins}")

with c3:
    st.warning("🗺 Most Active State")
    st.markdown(f"### {top_state}")
    st.caption(f"Constituencies : {top_state_count}")

st.divider()
# =====================================================
# DATASET EXPLORER
# =====================================================

st.subheader("📄 Dataset Explorer")

search = st.text_input(
    "🔍 Search Candidate / Constituency / Party"
)

display_data = filtered[
    [
        "year",
        "State",
        "Constituency",
        "Candidate",
        "Winning Party",
        "Party",
        "totvotpoll",
        "electors"
    ]
]

if search:

    display_data = display_data[
        display_data.astype(str)
        .apply(lambda col: col.str.contains(search, case=False))
        .any(axis=1)
    ]

st.dataframe(
    display_data,
    use_container_width=True,
    height=450
)

st.divider()
# =====================================================
# DOWNLOAD DATA
# =====================================================

csv = display_data.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="Election_Analysis.csv",
    mime="text/csv"
)

st.divider()
# =====================================================
# QUICK INSIGHTS
# =====================================================

st.subheader("📌 Dashboard Insights")

st.markdown(f"""
- 🏆 **{top_party}** is the most successful political party in the selected data.

- 👤 **{top_candidate}** has won the highest number of elections.

- 🗺 **{top_state}** contributes the highest number of constituencies.

- 🗳 A total of **{total_votes:,}** votes are represented in the filtered dataset.

- 👥 The dashboard currently covers **{total_candidates:,}** candidates.
""")

st.divider()
st.markdown(
    """
---
<center>

### 🗳 Political & Election Analysis Dashboard

Developed using **Python • Streamlit • Plotly • Scikit-Learn**

**Internship Project 2026**

</center>
""",
unsafe_allow_html=True
)