import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from app import load_data

st.title("🏷 Tag Cloud Analysis")

df = load_data()

tags = " ".join(df["tags"].dropna().astype(str))
wc = WordCloud(width=1200, height=600, background_color="white").generate(tags)

plt.figure(figsize=(12, 6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")

st.pyplot(plt)
