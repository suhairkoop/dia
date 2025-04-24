import streamlit as st
from gtts import gTTS
import tempfile
import os

st.set_page_config(page_title="Nara Dia – Cloud Voice", layout="centered")
st.title("🔊 Nara Dia – Web-based Voice Assistant")

text = st.text_area("What should Dia say?", height=100)

if st.button("Speak"):
    if text.strip():
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format='audio/mp3')
    else:
        st.warning("Please enter some text first.")


