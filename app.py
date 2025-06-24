import streamlit as st
from pytrends.request import TrendReq
import pandas as pd

# Page config
st.set_page_config(page_title="Market Entry Dashboard", page_icon="📈", layout="centered")

# Stylish title and subheader
st.title("AI-Driven Market Entry Strategy Dashboard")
st.markdown("Gain insights from Google Trends and AI-generated recommendations to plan your market entry.")

# User input
keyword = st.text_input("🔍 Enter a Product/Industry:", "Fitness Wearables")

if keyword:
    st.markdown(f"### Google Trends Analysis for **'{keyword}'**")

    # Google Trends Data
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], timeframe='today 12-m')

    data = pytrends.interest_over_time()

    if not data.empty:
        st.line_chart(data[keyword])
    else:
        st.warning("No Google Trends data found. Try another keyword.")

    # AI Placeholder Insight
    st.markdown("### 🤖 AI-Generated Market Insights")
    insight = f"""
    The market for **'{keyword}'** shows a growing trend in search interest.
    Emerging opportunities are noted in urban centers and tech-savvy demographics.
    Suggested entry via e-commerce and influencer marketing to capitalize on early adopters.
    """
    st.info(insight)

    # Market Entry Strategy
    st.markdown("### 🚀 Recommended Market Entry Strategy")
    st.success("""
    1. Launch through online platforms first to minimize costs.
    2. Collaborate with niche influencers for targeted reach.
    3. Offer early bird discounts to attract first movers.
    4. Expand to physical retail based on demand spikes.
    """)

# Footer
st.markdown("---")
st.caption("Built by Shaurya Jain • Market Insights Demo • 2025")


