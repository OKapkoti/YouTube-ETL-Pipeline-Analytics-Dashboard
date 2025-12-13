import streamlit as st
import plotly.express as px
from app import load_data

st.title("🌍 Region Insights")

df = load_data()
region_stats = df.groupby("region")["views"].sum()

fig = px.bar(
    x=region_stats.index,
    y=region_stats.values,
    title="Total Views by Region",
    labels={"x": "Region", "y": "Views"}
)

st.plotly_chart(fig, use_container_width=True)
