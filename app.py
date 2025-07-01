import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Market Entry Strategy Dashboard", layout="centered")

st.title("📊 Market Entry Strategy Dashboard")
st.markdown("Analyze consumer trend data to identify high-potential markets.")

# Load cached Google Trends-style data
@st.cache_data
def load_data():
    df = pd.read_csv("sample_trends_data.csv")
    df["Month"] = pd.to_datetime(df["Month"])
    return df

df = load_data()

# Dropdown to select trend focus
keyword = st.selectbox("Choose your market trend:", df.columns[1:])

# Plot interest over time
fig, ax = plt.subplots()
ax.plot(df["Month"], df[keyword], marker='o', color='green')
ax.set_title(f"Interest Over Time: {keyword}")
ax.set_xlabel("Month")
ax.set_ylabel("Search Interest")
ax.grid(True)
st.pyplot(fig)

# Show recommendation based on trend
latest_value = df[keyword].iloc[-1]
st.markdown("### 📈 AI Insight:")
if latest_value > 85:
    st.success(f"{keyword} shows a very strong upward trend — consider prioritizing this market!")
elif latest_value > 70:
    st.info(f"{keyword} is trending positively. Worth considering for entry.")
else:
    st.warning(f"{keyword} has a mild trend — proceed with deeper competitive analysis.")
