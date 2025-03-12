# Description: Test the trained model with an image.
# Load an image and run the model on it to see the results.

from ultralytics import YOLO

# Load trained model
model = YOLO("runs/pose/train2/weights/best.pt")

# Test the model with an image
results = model("images/squat-1.png", save=True) # here goes the path for your image

# Show result -> image with bounding boxes
for result in results:
    result.show()