# 🏥 Medical-AI Chest X-ray Viewer & Labeler Tool

A Python-based desktop application for viewing chest X-ray images, manually labeling them with disease types (e.g., Pneumonia), and saving labels in YAML format. Built with Tkinter, this project showcases foundational skills in medical AI data preparation and GUI development.


## 📌 Overview

This project was developed to explore **Medical AI and Machine Learning**. It simulates the early stages of an AI pipeline:

- Loading real-world medical imaging data
- Generating structured XML metadata
- Configuring behavior via `config.yaml`
- Building interactive tools for labeling
- Displaying labeled images in a viewer

The dataset uses publicly available chest X-ray images.

## 🔧 Features

- ✅ Interactive GUI for viewing chest X-ray images
- ✅ Manual labeling system (`Pneumonia`, `Tuberculosis`, `Normal`)
- ✅ YAML-based configuration and label storage
- ✅ XML metadata generation for each image
- ✅ Lightweight, beginner-friendly architecture
- ✅ Clean folder structure and reusable code


## 📁 Folder Structure
medical_ai_project/
│
├── config.yaml         # Configuration settings
├── process.py          # Generates XML metadata
├── labeler.py          # GUI for manual labeling
├── gui_viewer.py       # GUI for viewing labeled images
├── labels.yaml         # Saved image labels
├── README.md           # Project documentation
├── LICENSE             # MIT License
│
└── data/
├── images/         # Place .jpg chest X-ray images here
└── xml/            # Auto-generated XML metadata files


## 🖼️ Dataset Source

This project uses sample chest X-ray images from open-access datasets:

### 🔗 Dataset Sources:
- [NIH ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC)
- [COVID-19 Chest X-ray Dataset](https://github.com/ieee8023/covid-chestxray-dataset)

> ⚠️ **Note**: This project does **not include copyrighted images**. Download and place images in the `data/images/` directory.

---

## 🛠 Prerequisites

- Python 3.7+
- Pillow (image handling)
- PyYAML (config and label files)
- Tkinter (included with Python)

## 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

## 🙌 Contributions
Contributions are welcome! To improve the GUI, add features (e.g., CSV export, web support), or enhance documentation, please open a pull request.

## 📬 Want to Learn More?
Interested in building a web version, adding deep learning models, or creating a desktop app? Open an issue or contact me for guidance!

📚 Acknowledgments
Public chest X-ray datasets from NIH and IEEE
Open-source Python libraries: Tkinter, PIL, PyYAML
Inspiration from Elon Musk
