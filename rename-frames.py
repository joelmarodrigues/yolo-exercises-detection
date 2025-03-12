# This step is not this relevant, but it's useful to keep the frames organized.
# In order to train the model I need to have a lot of images of a person doing the squat exercise in diferent angles and positions.
# This way I can train the model to recognize the squat exercise in a more general way.
# To avoid collecting the images manually, I can use the frames extracted from the videos.

# This snippet renames the frames in a folder with the format: {video_folder}_{frame}.jpg.
# I made the mistake and this code helped me to fix it.
# DO NOT USE THIS CODE IF YOU DON'T NEED TO RENAME THE FRAMES.

import os

def rename_frames(folder_path):
    """renames frames in a folder with the format: {video_folder}_{frame}.jpg"""

    for video_folder in os.listdir(folder_path):
        video_folder_path = os.path.join(folder_path, video_folder)

        if os.path.isdir(video_folder_path):
            for filename in os.listdir(video_folder_path):
                if filename.endswith(".jpg"):  # Verifies if the file is a frame
                    old_path = os.path.join(video_folder_path, filename)
                    new_filename = f"{video_folder}_{filename}"
                    new_path = os.path.join(video_folder_path, new_filename)
                    os.rename(old_path, new_path)
                    print(f"Renamed: {old_path} → {new_path}")

    print("Renamed!")

# Example
frames_folder = "videos/squat/frames-squat"
rename_frames(frames_folder)