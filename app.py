import streamlit as st
import pandas as pd

# -------------------------
# Streamlit page config
# -------------------------
st.set_page_config(
    page_title="F1 2026 Australian GP Predictions",
    layout="wide"
)

st.title("🏎️ 2026 Australian GP - Predicted Race Results")

# -------------------------
# Load CSV from GitHub
# -------------------------
csv_url = "https://raw.githubusercontent.com/suhailahmed10/master/main/predicted_race_results.csv"

try:
    df_pred = pd.read_csv(csv_url)
    st.success("CSV loaded successfully!")
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    st.stop()

# -------------------------
# Top-3 Podium Table
# -------------------------
st.subheader("🏆 Predicted Podium")

# Get top 3 drivers
top3 = df_pred.sort_values("PredictedRacePos").head(3).reset_index(drop=True)
top3["Medal"] = ["🥇","🥈","🥉"]

# Display only relevant columns
top3_display = top3[["Medal","Driver","Constructor"]]

# Use st.dataframe to display cleanly without index
st.dataframe(top3_display, use_container_width=True)

# -------------------------
# Full Race Table
# -------------------------
st.subheader("📋 Full Race Results")

# Columns to display
full_table = df_pred[["Driver","Constructor","QualRank","QualTime","GapToPole","Grid"]]

# Display with gradient for readability
st.dataframe(full_table.style.background_gradient(cmap='viridis'), use_container_width=True)
