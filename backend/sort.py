from ultralytics import YOLO
import cv2
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort


keyToObject = {
    "0": "person",
    "1": "bicycle",
    "2": "car",
    "3": "motorcycle",
    "4": "airplane",
    "5": "bus",
    "6": "train",
    "7": "truck",
    "8": "boat",
    "9": "traffic light",
    "10": "fire hydrant",
    "11": "stop sign",
    "12": "parking meter",
    "13": "bench",
    "14": "bird",
    "15": "cat",
    "16": "dog",
    "17": "horse",
    "18": "sheep",
    "19": "cow",
    "20": "elephant",
    "21": "bear",
    "22": "zebra",
    "23": "giraffe",
    "24": "backpack",
    "25": "umbrella",
    "26": "handbag",
    "27": "tie",
    "28": "suitcase",
    "29": "frisbee",
    "30": "skis",
    "31": "snowboard",
    "32": "sports ball",
    "33": "kite",
    "34": "baseball bat",
    "35": "baseball glove",
    "36": "skateboard",
    "37": "surfboard",
    "38": "tennis racket",
    "39": "bottle",
    "40": "wine glass",
    "41": "cup",
    "42": "fork",
    "43": "knife",
    "44": "spoon",
    "45": "bowl",
    "46": "banana",
    "47": "apple",
    "48": "sandwich",
    "49": "orange",
    "50": "brocolli",
    "51": "carrot",
    "52": "hot dog",
    "53": "pizza",
    "54": "donut",
    "55": "cake",
    "56": "chair",
    "57": "couch",
    "58": "potted plant",
    "59": "bed",
    "60": "dining table",
    "61": "toilet",
    "62": "tv",
    "63": "laptop",
    "64": "mouse",
    "65": "remote",
    "66": "keyboard",
    "67": "cell phone",
    "68": "microwave",
    "69": "oven",
    "70": "toaster",
    "71": "sink",
    "72": "refrigerator",
    "73": "book",
    "74": "clock",
    "75": "vase",
    "76": "scissors",
    "77": "teddy bear",
    "78": "hair drier",
    "79": "toothbrush"
}

def getObject(keyToObject):
    with open("log.txt", "rb") as file:
        file.seek(-2, 2)  
        while file.read(1) != b'\n':
            file.seek(-2, 1)
        last_line = file.readline().decode()

        i = last_line.find(",")

        objectKey = last_line[i+1:-1]
    
    return (keyToObject[objectKey])

print(getObject(keyToObject))

def deepSort():
    global isRunning
    ## changed
    isRunning = True;

    warning_file = "log.txt"

    model = YOLO("yolo11n.pt")

    tracker = DeepSort(
        nms_max_overlap=1.0,
        max_iou_distance=0.7,
        max_age=70,
        n_init=3
    )

    camera = cv2.VideoCapture(1)

    # cv2.namedWindow("Camera Feed")

    #format: format, (previous size, object id)
    previous_sizes = {}


    #change this to increase warning threshold 
    size_increase_threshold = 1.1

    while True:
        ret, frame = camera.read()

        if not isRunning:
            break

        if not ret:
            print("Error: Could not capture image.")
            break
        
        frame = cv2.flip(frame, 1)

        results = model(frame, conf=0.78)
        detections = []

        for result in results:
            for box in result.boxes.xyxy: 
                x1, y1, x2, y2 = map(int, box[:4]) 
                conf = float(result.boxes.conf[0]) 
                cls = int(result.boxes.cls[0]) 
                if conf > 0.3:
                        detections.append(([x1, y1, x2, y2], conf, cls))

        tracks = tracker.update_tracks(detections, frame=frame)

        for track in tracks:
            if not track.is_confirmed():
                continue
            bbox = track.to_ltrb()  
            track_id = track.track_id 
            x1, y1, x2, y2 = map(int, bbox)

            current_width = x2 - x1
            current_height = y2 - y1
            current_size = current_width * current_height

            for det in detections:
                if det[0] == [x1, y1, x2, y2]:
                    cls = det[2]
                    break

            if track_id in previous_sizes:
                previous_size = previous_sizes[track_id]

                size_increase = current_size / previous_size
            
                if size_increase > size_increase_threshold:
                    with open(warning_file, "a") as file:
                        file.write(f"{track_id},{cls}\n")

            previous_sizes[track_id] = current_size
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'ID {track_id}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # print("detections", detections)
        # cv2.imshow("Camera Feed", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


def stopRunning():
    ##stop the loop
    global isRunning
    isRunning = False
