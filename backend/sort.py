from ultralytics import YOLO
import cv2
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort


def deepSort():
    model = YOLO("yolo11n.pt")

    tracker = DeepSort(
        nms_max_overlap=1.0,
        max_iou_distance=0.7,
        max_age=70,
        n_init=3
    )

    camera = cv2.VideoCapture(1)

    # cv2.namedWindow("Camera Feed")

    while True:
        ret, frame = camera.read()

        if not ret:
            print("Error: Could not capture image.")
            break
        
        frame = cv2.flip(frame, 1)

        results = model(frame, conf=0.15)
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
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'ID {track_id}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
        # cv2.imshow("Camera Feed", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

    camera.release()


    cv2.destroyAllWindows()
