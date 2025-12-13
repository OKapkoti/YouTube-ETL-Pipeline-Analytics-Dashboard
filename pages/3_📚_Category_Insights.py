import streamlit as st
import plotly.express as px
from app import load_data

st.title("📚 Category Insights")

df = load_data()
cat_stats = df.groupby("category_name")[["views", "likes", "comment_count"]].sum()

fig = px.bar(
    cat_stats,
    x=cat_stats.index,
    y="views",
    title="Total Views by Category"
)

fig.update_layout(xaxis_tickangle=45)
st.plotly_chart(fig, use_container_width=True)
