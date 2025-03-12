# Description: This script loads a trained YOLOv5 model and processes a video, drawing bounding boxes around detected objects.
# Choose a video file and run the script to see the model in action.

from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO("runs/pose/train/weights/best.pt")

# Load the video
video_path = "images/diagonal-squat.mp4"
cap = cv2.VideoCapture(video_path)

# Original video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Object to write the processed video
output_path = "images/result.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # codec to use
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Process each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # leave the loop when the video ends

    # Do the inference on the frame
    results = model(frame)

    # Draw the bounding boxes on the frame
    annotated_frame = results[0].plot()

    # Write the frame to the output video
    out.write(annotated_frame)

    # (Optional) Show the frame with the bounding boxes
    cv2.imshow("YOLOv8 Video", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # Press 'q' to quit
        break

# Free resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Video processed and saved on {output_path}")