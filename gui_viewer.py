
import os
import tkinter as tk
import yaml 
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET

# Load configuration from YAML
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

# List all processed images and their XML paths
image_dir = config['metadata']['image_dir']
xml_dir = config['metadata']['xml_dir']

# Get list of image filenames
image_filenames = os.listdir(image_dir)
image_paths = [os.path.join(image_dir, fname) for fname in image_filenames]

# Function to load and parse XML metadata
def load_metadata(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        metadata = {
            "FileName": root.find("FileName").text,
            "Disease": root.find("Disease").text,
            "Source": root.find("Source").text
        }
        return metadata
    except Exception as e:
        print(f"⚠️ Error parsing XML: {e}")
        return None

# Function to update the displayed image and metadata
def update_image(index):
    global current_index
    current_index = index

    # Clear previous image
    canvas.delete("all")

    # Load and display image
    img_path = image_paths[index]
    img = Image.open(img_path).convert('L')  # Convert to grayscale
    img = img.resize((400, 400))  # Resize for display
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(200, 200, image=photo)
    canvas.image = photo  # Keep a reference to prevent garbage collection

    # Load and display metadata
    xml_path = os.path.join(xml_dir, image_filenames[index].replace(".jpg", ".xml"))
    metadata = load_metadata(xml_path)
    if metadata:
        metadata_text.set(f"Filename: {metadata['FileName']}\n"
                         f"Disease: {metadata['Disease']}\n"
                         f"Source: {metadata['Source']}")
    else:
        metadata_text.set("No metadata available.")

# Function to go to previous image
def prev_image():
    global current_index
    if current_index > 0:
        update_image(current_index - 1)

# Function to go to next image
def next_image():
    global current_index
    if current_index < len(image_paths) - 1:
        update_image(current_index + 1)

# Initialize Tkinter window
root = tk.Tk()
root.title("Medical AI Image Viewer")

# Create main frame
frame = tk.Frame(root)
frame.pack(pady=20)

# Canvas for displaying images
canvas = tk.Canvas(frame, width=400, height=400, bg="white")
canvas.grid(row=0, column=0, padx=10, pady=10)

# Metadata text box
metadata_text = tk.StringVar()
metadata_label = tk.Label(frame, textvariable=metadata_text, font=("Arial", 12))
metadata_label.grid(row=0, column=1, padx=10, pady=10)

# Navigation buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

prev_button = tk.Button(button_frame, text="<< Previous", command=prev_image)
prev_button.pack(side=tk.LEFT, padx=5)

next_button = tk.Button(button_frame, text="Next >>", command=next_image)
next_button.pack(side=tk.RIGHT, padx=5)

# Initialize variables
current_index = 0

# Start by displaying the first image
update_image(current_index)

# Run the Tkinter event loop
root.mainloop()