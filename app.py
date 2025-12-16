import streamlit as st
import tempfile
from train import process_audio

st.set_page_config(page_title="Grammar Scoring Engine", layout="centered")

st.title("🎙️ Grammar Scoring Engine")
st.write("Upload an English audio file (.wav) to analyze grammar quality.")

uploaded_file = st.file_uploader("Upload audio file", type=["wav"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        temp_audio_path = tmp.name

    if st.button("Analyze Grammar"):
        with st.spinner("Analyzing audio..."):
            try:
                result = process_audio(temp_audio_path)

                st.subheader("📝 Recognized Text")
                st.write(result["text"])

                st.subheader("📊 Grammar Analysis")
                st.write(f"**Words:** {result['words']}")
                st.write(f"**Errors:** {result['errors']}")
                st.write(f"**Grammar Score:** {result['score']} / 100")

            except Exception as e:
                st.error(f"Error: {e}")
