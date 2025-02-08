import speech_recognition as sr
from openai import OpenAI
from tts import *
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def chat_with_gpt(prompt):
    """Send user input to GPT-4o-mini and return the streamed response."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=False  # Enable streaming
    )

    full_response = response.choices[0].message.content

    print(f"AI: {full_response}")  # Print the full response at once
    return full_response

    # for chunk in response:
    #     if chunk.choices and chunk.choices[0].delta.get("content"):
    #         text_chunk = chunk.choices[0].delta["content"]
    #         full_response += text_chunk
    #         print(text_chunk, end="", flush=True)


recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            speak("where are you headed?")
            recognizer.adjust_for_ambient_noise(mic, duration=0.5)
            audio = recognizer.listen(mic, timeout = 5, phrase_time_limit=8)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")
            stored_result = text
            print(f"Final Stored Result: {stored_result}")
            break  

    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
    
destination = chat_with_gpt("return ONLY The destination the user is looking based on this input:" + stored_result)

speak("Okay, navigating to" + destination)

# speak(ai_response)

# speak("okay, navigating to" + text)


