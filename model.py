import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)

def voice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print("you said",text)
            return text
        except sr.UnknownValueError:
            print("sorry could not understand the audio")
        except sr.RequestError as e:
            print("could not get result from the google text to speech service")

def model(user_input):
    from google import genai
    client=genai.Client()
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[{
            "role": "user",
            "parts": [{
                "text": user_input  # Ensure the input is wrapped in 'text' key
            }]
        }]
    )
    result=response.text
    return result
    
import tempfile

def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tts.save(tmp_file.name)  
        tmp_file.seek(0)  
        audio_data = tmp_file.read()  
    
    
    os.remove(tmp_file.name)
    
    return audio_data

