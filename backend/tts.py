import os
import subprocess
from dotenv import load_dotenv
from cartesia import Cartesia

load_dotenv()

CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")

if os.environ.get("CARTESIA_API_KEY") is None:
    raise ValueError("CARTESIA_API_KEY is not set")

client = Cartesia(api_key=os.environ.get("CARTESIA_API_KEY"))

def speak(text):
    """Generate speech from text using Cartesia API and play it."""
    
    # Generate audio with Cartesia API
    data = client.tts.bytes(
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

# Example usage:
if __name__ == "__main__":
    script_text = "The object is approaching. Please be careful!"
    speak(script_text)


# CARTESIA_API_URL = "https://api.cartesia.com/tts"
# API_KEY = "sk_car_jpjvcsL4KLLV-Q29c_BcI"

# def speak():
#     """Speaks the detected object and its distance in feet."""
#     engine = pyttsx3.init()

#     # Construct the speech text
#     # text = f"The {object_name} is {approaching:.1f} you."
#     text = ("""Start Address: 5000 Forbes Ave, Pittsburgh, PA 15213, USA 
#             End Address: 300 S Craig St Suite 101, Pittsburgh, PA 15213, USA
#             Instruction: Head <b>north</b> toward <b>Forbes Ave</b>
#             Distance: 20 ft
#             Duration: 1 min
#             Instruction: Turn <b>left</b> onto <b>Forbes Ave</b>
#             Distance: 0.1 mi
#             Duration: 3 mins
#             Instruction: Turn <b>right</b> onto <b>S Craig St</b><div style= >
#             Destination will be on the right</div>""")
    
#     # Speak out loud
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     speak()
# # example for Alex:
# # if __name__ == "__main__":
# #     # write variable below, insert it in a while loop in main
# #     speak("no wayyy", 3)
