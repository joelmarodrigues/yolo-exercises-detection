# Description: This script is used to train the YOLO model using the dataset.
# The dataset is a YAML file that contains the path to the images and the annotations.
# Remember I trained the model with the squat-skeleton dataset, which was classified into 3 main classes: squat, hal-squat and standing.
# I used Roboflow to create the dataset and export it as a YOLOv8 format.
# The dataset is located in the 'datasets' folder.

import os
from ultralytics import YOLO

# Main function: I had to add this loop to avoid parallelism problems I encountered in Windows.
if __name__ == "__main__":
    # dataset path
    dataset_path = "C:/Users/joelm/PycharmProjects/exercises-model/yolo-model/datasets/squat-skeleton.v2i.yolov8/data.yaml"

    # Error handling: check if dataset exists
    if os.path.exists(dataset_path):
        print(f"✅ Dataset found: {dataset_path}")
    else:
        raise FileNotFoundError(f"❌ ERROR: The '{dataset_path}' wasa NOT found!")

    # load model from ultralytics = YOLO("yolov8n-pose.pt")
    model = YOLO("yolov8n-pose.pt")

    # Train the model
    model.train(
        data=dataset_path,      # path to dataset
        epochs=100,             # epochs is the number of iterations
        batch=16,               # batch is the number of images per iteration
        imgsz=1280,             # 1280 is the image size
        lr0=0.005,              # Learning rate = is the rate at which the model learns
        weight_decay=0.0005,    # Reduce overfitting
        device="cuda"           # use GPU if available or CPU(default)
    )