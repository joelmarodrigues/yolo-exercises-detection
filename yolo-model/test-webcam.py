# With this script, you can test the YOLOv5 model on your webcam in real-time.
# Stand in front of the camera and do the squat exercise.
# The model will draw bounding boxes around you. And hopefully recognize the squat exercise.

from ultralytics import YOLO
import cv2

# Model
model = YOLO("runs/pose/train2/weights/best.pt")

# Open webcam (default) -> 0 or 1 for external cameras
cap = cv2.VideoCapture(0)

# Defines camera resolution
cap.set(3, 640)  # width
cap.set(4, 480)  # height

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # leaves the loop when the video ends

    # Inferencing on the frame
    results = model(frame)

    # Draw the bounding boxes on the frame
    annotated_frame = results[0].plot()

    # Show the frame in real-time
    cv2.imshow("YOLOv8 Live", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Free resources: camera and windows
cap.release()
cv2.destroyAllWindows()