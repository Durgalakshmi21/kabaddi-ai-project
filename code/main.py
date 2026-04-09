"""import cv2
import os

# Input video path
video_path = "../videos/sample.mp4"

# Output folder
output_folder = "../frames"

# Create folder if not exists
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save every 10th frame (to reduce data)
    if count % 10 == 0:
        cv2.imwrite(f"{output_folder}/frame_{count}.jpg", frame)

    count += 1

cap.release()
print("Frames extracted successfully!")
"""
"""import cv2
import os

import random


def detect_event():
    events = ["raid_start", "tackle", "bonus", "idle"]
    return random.choice(events)

def generate_commentary(event):
    if event == "raid_start":
        return "Raider enters the opponent's half!"

    elif event == "tackle":
        return "Excellent tackle by defenders!"

    elif event == "bonus":
        return "Bonus point secured!"

    else:
        return "Game in progress."

# -------- STEP 1: Extract Frames -------- #

video_path = "../videos/sample.mp4"
frames_folder = "../frames"

# Create frames folder if not exists
os.makedirs(frames_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Cannot open video")
    exit()

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save every 10th frame
    if count % 10 == 0:
        cv2.imwrite(f"{frames_folder}/frame_{count}.jpg", frame)

    count += 1

cap.release()
print("Frames extracted successfully!")

# -------- STEP 2: Playback Frames -------- #

frames = sorted(os.listdir(frames_folder))

print("Total frames:", len(frames))

for frame_file in frames:
    path = os.path.join(frames_folder, frame_file)
    frame = cv2.imread(path)

    if frame is None:
        continue

    # Get event + commentary
    event = detect_event()
    comment = generate_commentary(event)

    # Show commentary on video
    cv2.putText(frame, comment, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Playback", frame)

    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
"""
import cv2
import os
import random
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

# -------- EVENT + COMMENTARY -------- #

def detect_event():
    events = ["raid_start", "tackle", "bonus", "idle"]
    return random.choice(events)

def generate_commentary(event):
    if event == "raid_start":
        return "Raider enters the opponent's half!"

    elif event == "tackle":
        return "Excellent tackle by defenders!"

    elif event == "bonus":
        return "Bonus point secured!"

    else:
        return "Game in progress."

# -------- STEP 1: Extract Frames -------- #

video_path = "../videos/sample.mp4"
frames_folder = "../frames"

os.makedirs(frames_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Cannot open video")
    exit()

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save every 10th frame
    if count % 10 == 0:
        cv2.imwrite(f"{frames_folder}/frame_{count}.jpg", frame)

    count += 1

cap.release()
print("Frames extracted successfully!")

# -------- STEP 2: Playback + Commentary -------- #

frames = sorted(os.listdir(frames_folder))
print("Total frames:", len(frames))

previous_event = None
frame_counter = 0

for frame_file in frames:
    path = os.path.join(frames_folder, frame_file)
    frame = cv2.imread(path)

    if frame is None:
        continue

    # Detect event
    event = detect_event()
    comment = generate_commentary(event)

    # Show commentary on screen FIRST
    cv2.putText(frame, comment, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Playback", frame)

    # 🔊 Speak AFTER video starts (fixes your issue)
    if event != previous_event and frame_counter > 5:
        engine.say(comment)
        engine.runAndWait()
        previous_event = event

    frame_counter += 1

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()