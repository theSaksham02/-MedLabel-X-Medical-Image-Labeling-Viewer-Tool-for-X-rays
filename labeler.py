import os
import tkinter as tk
import yaml
from PIL import Image, ImageTk

# Load configuration
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

image_dir = config['metadata']['image_dir']
label_file = "labels.yaml"

# Get list of image files
image_files = sorted(os.listdir(image_dir))
total_images = len(image_files)
print(f"Found {total_images} images for labeling.")

# Dictionary to store user labels
labels = {}

# Function to save labels to YAML
def save_labels():
    with open(label_file, 'w') as f:
        yaml.dump(labels, f)
    print(f"✅ Labels saved to {label_file}")

# Function to load current image
def load_image(index):
    img_path = os.path.join(image_dir, image_files[index])
    img = Image.open(img_path).convert('L')  # Grayscale
    img = img.resize((400, 400))
    photo = ImageTk.PhotoImage(img)
    panel.configure(image=photo)
    panel.image = photo  # Keep reference
    update_status(index)

# Update status text
def update_status(index):
    status_label.config(text=f"Image {index+1}/{total_images}: {image_files[index]}")

# Label buttons
def set_label(label):
    global current_index
    filename = image_files[current_index]
    labels[filename] = label
    print(f"📌 Labeled '{filename}' as '{label}'")
    next_image()

# Go to next image
def next_image():
    global current_index
    if current_index < total_images - 1:
        current_index += 1
        load_image(current_index)
    else:
        status_label.config(text="🎉 You've labeled all images!")

# Go to previous image
def prev_image():
    global current_index
    if current_index > 0:
        current_index -= 1
        load_image(current_index)

# Initialize Tkinter window
root = tk.Tk()
root.title("Medical Image Labeler")

# Image panel
panel = tk.Label(root)
panel.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=5)

# Label buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Pneumonia", width=12, bg="lightcoral", command=lambda: set_label("Pneumonia")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Tuberculosis", width=12, bg="lightblue", command=lambda: set_label("Tuberculosis")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Normal", width=12, bg="lightgreen", command=lambda: set_label("Normal")).pack(side=tk.LEFT, padx=5)

# Navigation buttons
nav_frame = tk.Frame(root)
nav_frame.pack(pady=10)

tk.Button(nav_frame, text="<< Previous", command=prev_image).pack(side=tk.LEFT, padx=5)
tk.Button(nav_frame, text="Next >>", command=next_image).pack(side=tk.RIGHT, padx=5)

# Save button
save_btn = tk.Button(root, text="💾 Save All Labels", command=save_labels)
save_btn.pack(pady=10)

# Start labeling
current_index = 0
load_image(current_index)

# Run app
root.mainloop()