import streamlit as st
from app import load_data

st.title("🏠 Home Dashboard")

df = load_data()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Views", f"{df['views'].sum():,}")
c2.metric("Total Likes", f"{df['likes'].sum():,}")
c3.metric("Total Comments", f"{df['comment_count'].sum():,}")
c4.metric("Total Videos", f"{len(df):,}")

st.write("---")

st.subheader("🎬 Videos per Category")
st.bar_chart(df["category_name"].value_counts())
