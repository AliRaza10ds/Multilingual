import streamlit as st
from model import voice,model,text_to_speech
import time
from gtts import gTTS

#def main():
st.title("Multilingual AI Assistant")
st.markdown("just click on **Ask me anything** and speak your query")
if st.button("Ask me anything"):
        try:
         with st.spinner("Listening...."):
            text=voice()
            with st.spinner("Generating Response"):
                response=model(text)
                st.success("AI Response")
                text_to_speech(response)
                st.write("you asked:",text)
                st.write("AI says:",response)
                audio_bytes=text_to_speech(response,lang='en')
                st.audio(audio_bytes,format="audio/mp3")
        except Exception as e:
            st.error(f"something went wrong:{e}")

