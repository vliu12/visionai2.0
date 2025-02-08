import requests
import re
import geocoder
from datetime import datetime
import time
import os
import subprocess

instructions = []
timer = []
distance = []

# Define the API endpoint and parameters
url = "https://maps.googleapis.com/maps/api/directions/json"
params = {
    "origin": "Carnegie Mellon University",
    "destination": "Wushiland Boba - S Craig St (CMU)",
    "mode": "walking",
    "key": "AIzaSyDUId9XbwIt4TX-Sat7HqAJRpIhmuHc_CE"
}

# Send GET request to the API
response = requests.get(url, params=params)

# Parse the JSON response
data = response.json()

def remove_html_tags(text):
    return re.sub(r'<[^>]*>', '', text)

def get_location():
    g = geocoder.ip('me')  # 'me' gets your IP-based location
    if g.ok:
        print(f"Latitude: {g.latlng[0]}")
        print(f"Longitude: {g.latlng[1]}")
    else:
        print("Geolocation could not be determined.")

def printWithTime(data, distance, instructions, timer):
    start_time = time.time()  # Record the start time

    i = 0
    for timing in range(len(timer)):
        minutes = int(timer[timing].split(" ")[0])
        seconds = minutes*60
        time.sleep(10)
        print('starting navigation!')

        print(f'{instructions[i]}')
        print(f'{seconds} seconds')
        
        time.sleep(seconds * 1.05) 

        i += 1

        elapsed_time = time.time() - start_time  
        if elapsed_time >= 800:  
            print("Timed Out.")
            break  

def process_directions(data):
    if data["status"] == "OK":
        # Initialize empty lists to store the instructions, distances, and durations
        instructions = []
        distance = []
        timer = []

        # Print out relevant details (e.g., directions)
        for leg in data["routes"][0]["legs"]:
            print(f"Start Address: {leg['start_address']}")
            print(f"End Address: {leg['end_address']}")
            for step in leg["steps"]:
                # Remove HTML tags from the instruction
                instruction = remove_html_tags(step['html_instructions'])
                instructions.append(instruction)
                # print(f"Instruction: {instruction}")
                
                # Print out distance and append it to the list
                # print(f"Distance: {step['distance']['text']}")
                distance.append(step['distance']['text'])
                
                # Print out duration and append it to the list
                # print(f"Duration: {step['duration']['text']}")
                timer.append(step['duration']['text'])

        # Return the lists if you want to use them later
        return instructions, distance, timer
    else:
        print("Error: ", data["status"])
        return None, None, None

# get_location()
instructions, distance, timer = process_directions(data)

printWithTime(data, distance, instructions, timer)

print(instructions)
print(distance)
print(timer)
