
import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="News Summarizer", layout="centered")
st.title("📰 News Article Summarizer")

st.write("Paste your news article below and get a quick summary using AI!")

# Text input
article = st.text_area("📝 Paste the news article text here:", height=300)

# On clicking Summarize
if st.button("Summarize Article"):
    if article.strip():
        with st.spinner("Summarizing..."):
            summary = summarize_text(article)
        st.subheader("✂ Summary")
        st.success(summary)
    else:
        st.warning("⚠ Please paste the article text first!")
