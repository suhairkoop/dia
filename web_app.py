
import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Nara Dia", layout="centered")
st.title("🎙️ Nara Dia – AI Voice Assistant")

text = st.text_area("What should Dia say?", height=100)

if st.button("Generate Voice"):
    if text.strip():
        output_path = "response.wav"
        result = subprocess.run(
            ["python", "cli.py", text, "--output", output_path],
            capture_output=True,
            text=True
        )
        if result.returncode == 0 and os.path.exists(output_path):
            st.audio(output_path)
        else:
            st.error("Something went wrong.")
            st.code(result.stderr)
    else:
        st.warning("Enter some text first.")




import streamlit as st
import pyttsx3
import tempfile
import os

st.set_page_config(page_title="Nara Dia – Local Voice", layout="centered")
st.title("🗣️ Nara Dia – Instant Voice Assistant")

text = st.text_area("What should Dia say?", height=100)

if st.button("Speak"):
    if text.strip():
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
            engine.save_to_file(text, fp.name)
            engine.runAndWait()
            st.audio(fp.name)
    else:
        st.warning("Please enter some text first.")


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


