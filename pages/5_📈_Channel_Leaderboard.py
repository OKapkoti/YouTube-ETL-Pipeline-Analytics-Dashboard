import streamlit as st
from app import load_data

st.title("📈 Channel Leaderboard")

df = load_data()

leaderboard = (
    df.groupby("channel_title")[["views", "likes", "comment_count"]]
    .sum()
    .sort_values("views", ascending=False)
    .head(20)
)

st.dataframe(leaderboard)
