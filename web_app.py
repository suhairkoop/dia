
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




