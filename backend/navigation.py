import requests
import re
import geocoder
import time
from speak import TextToSpeech

class Navigation:
    def __init__(self, origin, destination, mode="walking", api_key="YOUR_API_KEY"):
        self.origin = origin
        self.destination = destination
        self.mode = mode
        self.api_key = api_key
        self.instructions = []
        self.timer = []
        self.distance = []
        self.tts = TextToSpeech()
        self.data = self.get_directions()
    
    def get_directions(self):
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": self.origin,
            "destination": self.destination,
            "mode": self.mode,
            "key": self.api_key
        }
        response = requests.get(url, params=params)
        return response.json()
    
    @staticmethod
    def remove_html_tags(text):
        return re.sub(r'<[^>]*>', '', text)
    
    def get_location(self):
        g = geocoder.ip('me')
        if g.ok:
            print(f"Latitude: {g.latlng[0]}")
            print(f"Longitude: {g.latlng[1]}")
        else:
            print("Geolocation could not be determined.")
    
    def process_directions(self):
        if self.data["status"] == "OK":
            for leg in self.data["routes"][0]["legs"]:
                print(f"Start Address: {leg['start_address']}")
                print(f"End Address: {leg['end_address']}")
                for step in leg["steps"]:
                    instruction = self.remove_html_tags(step['html_instructions'])
                    self.instructions.append(instruction)
                    self.distance.append(step['distance']['text'])
                    self.timer.append(step['duration']['text'])
        else:
            print("Error: ", self.data["status"])
    
    def start_navigation(self):
        self.process_directions()
        start_time = time.time()
        self.tts.speak(f'Starting navigation to {self.destination}!')

        for i in range(len(self.timer)):
            minutes = int(self.timer[i].split(" ")[0])
            seconds = minutes * 60
            time.sleep(10)  # Short delay before speaking
            self.tts.speak(self.instructions[i])
            print(f'{seconds} seconds')
            time.sleep(seconds * 1.05)
            
            if time.time() - start_time >= 800:
                self.tts.speak("An unexpected error occurred. Timed out.")
                break

# Example Usage
if __name__ == "__main__":
    navigator = Navigation("Carnegie Mellon University", "Wushiland Boba - S Craig St (CMU)", api_key="AIzaSyDUId9XbwIt4TX-Sat7HqAJRpIhmuHc_CE")
    navigator.start_navigation()
