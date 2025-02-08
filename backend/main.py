
import uvicorn
import os
print("current working directory: ", os.getcwd())
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sort
from navigation import Navigation

from ultralytics import YOLO
import cv2


# Getting data from Maggie's Open CV --> arrays of things and identified objects
# in here i do the deep sort --> give us displacement so we can calculate area of image which shows the distance between us and the thing
# 

navigator = Navigation("Carnegie Mellon University", "Wushiland Boba - S Craig St (CMU)", api_key="AIzaSyDUId9XbwIt4TX-Sat7HqAJRpIhmuHc_CE")
# navigator.start_navigation()


## it can automatically validate data coming in and it
## can format data going out based on Pydantic models
class Fruit(BaseModel):
    name: str

class Fruits(BaseModel):
    fruits: List[Fruit]

app = FastAPI()

origins = [
    "http://localhost:8081"
]

## CORS = Cross-Origin Resource Sharing

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/classify")
def classify():
    sort.deepSort()

@app.get("/stopClassify")
def stopClassify():
    sort.stopRunning()

@app.get("/navigate")
def navigate():
    navigator.start_navigation()



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)