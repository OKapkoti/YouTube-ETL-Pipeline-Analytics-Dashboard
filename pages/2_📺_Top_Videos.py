import streamlit as st
import plotly.express as px
from app import load_data

st.title("📺 Top Videos")

df = load_data()
top = df.nlargest(20, "views")

fig = px.bar(
    top,
    x="title",
    y="views",
    color="category_name",
    title="Top 20 Most Viewed Videos"
)

fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)
