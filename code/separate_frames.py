import os
import shutil
import pandas as pd

# ===== Paths =====
frames_folder = "../dataset/frames"          # folder with all your frames
csv_path = "../dataset/final_labels.csv"     # labeled CSV
output_folder = "../dataset/frames_by_action"  # folder to store separated frames

# ===== Load CSV safely =====
try:
    data = pd.read_csv(csv_path)
    print("CSV loaded successfully!")
except FileNotFoundError:
    print(f"Error: CSV file not found at {csv_path}")
    exit()

# ===== Check CSV columns =====
print("Columns in CSV:", data.columns.tolist())

# ===== Ask user for correct columns =====
frame_col = input("Enter the column name for frame filenames: ")
label_col = input("Enter the column name for labels/actions: ")

# ===== Create folders for each action =====
actions = data[label_col].unique()
for action in actions:
    action_path = os.path.join(output_folder, action)
    os.makedirs(action_path, exist_ok=True)

# ===== Copy frames to their action folder =====
missing_frames = 0
for index, row in data.iterrows():
    frame_file = row[frame_col]       # get filename from CSV
    action_label = row[label_col]     # get label from CSV

    src_path = os.path.join(frames_folder, frame_file)
    dst_path = os.path.join(output_folder, action_label, frame_file)

    if os.path.exists(src_path):
        shutil.copy(src_path, dst_path)  # copy to keep original frames
    else:
        print(f"Warning: {frame_file} not found in {frames_folder}")
        missing_frames += 1

print(f"Frames separated by action successfully! Missing frames: {missing_frames}")