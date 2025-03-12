# Description: Extracts frames from videos in a folder and saves them in another folder.
# Use it if you need to train your own model, and you don't have the images yet.
# But for these project the model was already trained.

import imageio
import os

# the imageio library is used to read the frames from the videos and save them as images.
# Example: if the frame_interval is 10, the function will save 1 frame every 10 frames.
# This way, the function will save fewer frames and the images will be more diverse.

def extract_frames_from_videos(video_folder, output_folder, frame_interval=10):
    """Extracts frames from videos in a folder and saves them in another folder."""
    os.makedirs(output_folder, exist_ok=True)

    video_files = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

    for video_file in video_files:
        video_path = os.path.join(video_folder, video_file)
        reader = imageio.get_reader(video_path, "ffmpeg")

        frame_count = 0
        saved_count = 0
        video_output_folder = os.path.join(output_folder, video_file.split(".")[0])
        os.makedirs(video_output_folder, exist_ok=True)

        for frame in reader:
            if frame_count % frame_interval == 0:
                frame_filename = os.path.join(video_output_folder, f"frame_{saved_count}.jpg")
                imageio.imwrite(frame_filename, frame)
                saved_count += 1
                print(f"Frame salvo: {frame_filename}")

            frame_count += 1

    print("Extraction done!")


# Example
video_folder = "videos/squat"
output_folder = "videos/squat/frames-squat"
extract_frames_from_videos(video_folder, output_folder)