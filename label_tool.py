import cv2
import os

video_folder = r"D:\kabaddi videos\Kabaddi_Commentary_Dataset_v1\clips\clips_small"
output_file = "my_labels.csv"

if not os.path.exists(output_file):
    with open(output_file, "w") as f:
        f.write("clip_id,action\n")

videos = [v for v in os.listdir(video_folder) if v.endswith(".webm")]
videos.sort()

print("Total videos:", len(videos))
print("SPACE = default (raid) | t=tackle | b=bonus | o=out | i=idle | q=quit")

default_label = "raid"   # 👈 YOU CAN CHANGE THIS

for video in videos:
    path = os.path.join(video_folder, video)
    cap = cv2.VideoCapture(path)

    print("\nPlaying:", video)
    label = None

    while True:
        ret, frame = cap.read()

        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        cv2.imshow("Video", frame)
        key = cv2.waitKey(30) & 0xFF

        if key == 32:  # SPACE key
            label = default_label
        elif key == ord('t'):
            label = "tackle"
        elif key == ord('b'):
            label = "bonus"
        elif key == ord('o'):
            label = "out"
        elif key == ord('i'):
            label = "idle"
        elif key == ord('q'):
            exit()

        if label is not None:
            with open(output_file, "a", newline='', encoding='utf-8') as f:
                f.write(f"{video},{label}\n")

            print(f"Saved: {video} -> {label}")
            break

    cap.release()

cv2.destroyAllWindows()