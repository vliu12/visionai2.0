import os
import subprocess
from dotenv import load_dotenv
from cartesia import Cartesia

load_dotenv()

class TextToSpeech:
    def __init__(self):
        """Initialize the TextToSpeech class with the Cartesia API client."""
        CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
        if CARTESIA_API_KEY is None:
            raise ValueError("CARTESIA_API_KEY is not set")

        self.client = Cartesia(api_key=CARTESIA_API_KEY)

    def speak(self, text):
        """Generate speech from text using Cartesia API and play it."""
        # Generate audio with Cartesia API
        data = self.client.tts.bytes(
            model_id="sonic-english",
            transcript=text,  # Using passed text variable
            voice_id="694f9389-aac1-45b6-b726-9d9369183238",  # Barbershop Man
            output_format={
                "container": "wav",
                "encoding": "pcm_f32le",
                "sample_rate": 44100,
            },
        )

        # Save the generated speech
        audio_file = "output.wav"
        with open(audio_file, "wb") as f:
            f.write(data)

        # Play the generated speech
        subprocess.run(["ffplay", "-autoexit", "-nodisp", audio_file])

