import cv2
import os
import pandas as pd

# Load labels
labels_df = pd.read_csv("dataset/my_labels.csv")

video_folder = "dataset/videos"   # <-- put your videos here
output_folder = "dataset/frames"

os.makedirs(output_folder, exist_ok=True)

for index, row in labels_df.iterrows():
    video_name = row["clip_id"]
    action = row["action"]

    video_path = os.path.join(video_folder, video_name)

    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    save_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Extract every 10th frame
        if frame_count % 10 == 0:
            frame = cv2.resize(frame, (224, 224))

            frame_name = f"{video_name[:-5]}_{save_count}.jpg"
            save_path = os.path.join(output_folder, action)

            os.makedirs(save_path, exist_ok=True)

            cv2.imwrite(os.path.join(save_path, frame_name), frame)
            save_count += 1

        frame_count += 1

    cap.release()

print("Frame extraction completed ✅")