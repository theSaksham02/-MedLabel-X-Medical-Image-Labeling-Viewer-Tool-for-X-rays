# Medical-AI Mini Project

A simple project that uses:
- **YAML** for configuration
- **XML** for metadata
- **Python** for downloading and displaying real-world chest X-ray images

## Features

- Downloads chest X-ray images from a public dataset
- Creates XML metadata for each image
- Displays images in grayscale (black and white)
- Uses clean YAML config

## Tools Used

- `yaml`
- `xml.etree.ElementTree` (Python's built-in library for XML parsing)
- `requests`
- `PIL`
- `matplotlib` (Python library for creating static, animated, and interactive visualizations)

## Setup

```bash
pip install PyYAML requests pillow matplotlib
python process.py