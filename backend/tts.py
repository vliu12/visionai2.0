import pyttsx3

def speak(object_name, distance):
    """Speaks the detected object and its distance in feet."""
    engine = pyttsx3.init()

    # Construct the speech text
    text = f"The {object_name} is {distance:.1f} feet away."
    
    # Speak out loud
    engine.say(text)
    engine.runAndWait()

# example for Alex:
# if __name__ == "__main__":
    # write variable below, insert it in a while loop in main
    # speak("")
