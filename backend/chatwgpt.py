import speech_recognition as sr
from openai import OpenAI
from tts import *
from dotenv import load_dotenv
import os

class GPTSpeechAssistant:
    def __init__(self):
        load_dotenv()
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.OPENAI_API_KEY)
        self.recognizer = sr.Recognizer()

    def chat_with_gpt(self, prompt):
        """Send user input to GPT-4o-mini and return the streamed response."""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            stream=False  # Enable streaming
        )
        full_response = response.choices[0].message.content
        print(f"AI: {full_response}")  # Print the full response at once
        return full_response

    def listen_for_destination(self):
        """Listen for the user's spoken destination."""
        while True:
            try:
                with sr.Microphone() as mic:
                    speak("Where are you headed to?")
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.5)
                    audio = self.recognizer.listen(mic, timeout=5, phrase_time_limit=8)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    print(f"Recognized {text}")
                    stored_result = text
                    print(f"Final Stored Result: {stored_result}")
                    return stored_result

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that. Please try again.")
                continue

    def get_destination_from_gpt(self, user_input):
        """Get the destination from GPT-4o-mini using the user's input."""
        prompt = f"Using the following sentence, give me the destination that the user is asking for, and that's it: {user_input}"
        destination = self.chat_with_gpt(prompt)
        return destination

    def assist_user(self):
        """Main function to drive the assistant's process."""
        # Step 1: Listen for destination from user
        user_input = self.listen_for_destination()

        # Step 2: Get the destination from GPT
        destination = self.get_destination_from_gpt(user_input)

        # Step 3: Confirm with the user
        speak(f"Okay, navigating to {destination}")

if __name__ == "__main__":
    assistant = GPTSpeechAssistant()
    assistant.assist_user()
