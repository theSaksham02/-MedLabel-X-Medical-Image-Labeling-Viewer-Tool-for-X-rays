# Import libraries
import os
import yaml
from PIL import Image
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

# Load YAML config
with open("config.yaml", 'r') as f:
    config = yaml.safe_load(f)

# Create folders if they don't exist
os.makedirs(config['metadata']['xml_dir'], exist_ok=True)
os.makedirs(config['metadata']['image_dir'], exist_ok=True)

# Function to create XML metadata
def create_xml_metadata(image_name, disease="Pneumonia"):
    root = ET.Element("Image")
    ET.SubElement(root, "FileName").text = image_name
    ET.SubElement(root, "Disease").text = disease
    ET.SubElement(root, "Source").text = "Local Chest X-ray Dataset"
    tree = ET.ElementTree(root)
    xml_path = os.path.join(config['metadata']['xml_dir'], image_name.replace(".jpg", ".xml"))
    try:
        tree.write(xml_path)
        print(f"✅ Created XML: {xml_path}")
        return xml_path
    except Exception as e:
        print(f"🚨 Failed to write XML for {image_name}: {e}")
        return None

#Change: We will no longer show images one-by-one inside the loop 

# Main loop
total_images = len(config['dataset']['sample_images'])
print(f"\n🔄 Found {total_images} images in config. Starting processing...\n")

#Change: Create a list to hold the paths of successfully processed images
processed_image_paths = []

for i, fname in enumerate(config['dataset']['sample_images']):
    print(f"\n[{i+1}/{total_images}] Processing '{fname}'")

    # Build full path
    image_path = os.path.join(config['metadata']['image_dir'], fname)

    # Check if file exists
    if not os.path.exists(image_path):
        print(f"⚠️ File not found: {image_path}")
        continue

    # Try to open file early
    try:
        with open(image_path, 'rb') as f:
            f.read(10) # Read first 10 bytes to check readability
        print(f"✅ Successfully read header of {image_path}")
    except Exception as e:
        print(f"🚫 Cannot read image file: {image_path} | Error: {e}")
        continue

    # Generate XML
    xml_path = create_xml_metadata(fname)
    if not xml_path:
        continue

    # Parse XML to confirm
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        disease = root.find("Disease").text
        print(f"    ✅ Disease: {disease}")
    except Exception as e:
        print(f"❗ Failed to parse XML {xml_path}: {e}")
        continue

    #Change: Add the valid image path to our list for later display
    processed_image_paths.append(image_path)


print("\n✅ Done processing all images.")

#Change: New section to display all images together at the end
if config['output']['show_images'] and processed_image_paths:
    print(f"\n🖼️ Displaying {len(processed_image_paths)} images...")
    
    num_images = len(processed_image_paths)
    cols = 4  # Number of columns in the grid
    rows = (num_images + cols - 1) // cols  # Calculate rows needed

    fig, axes = plt.subplots(rows, cols, figsize=(15, 4 * rows))
    axes = axes.flatten()  # Flatten the grid of axes for easy iteration

    for i, img_path in enumerate(processed_image_paths):
        try:
            img = Image.open(img_path)
            ax = axes[i]
            ax.imshow(img, cmap='gray')
            ax.set_title(os.path.basename(img_path), fontsize=10)
            ax.axis('off')
        except Exception as e:
            print(f"❌ Error displaying image {img_path}: {e}")
            axes[i].set_title(f"Error: {os.path.basename(img_path)}", fontsize=8)
            axes[i].axis('off')

    # Hide any unused subplots
    for i in range(num_images, len(axes)):
        axes[i].axis('off')

    plt.tight_layout()
    plt.show() # This one call will now display the entire grid