# Repository Overview: Image Resizer Script

This repository contains a Python script for resizing and padding images. The script allows users to match the size of a batch of images to the dimensions of a reference image. It offers flexibility in usage with command line arguments or a configuration file.

## Features
- Resizes images to match the height of a reference image while maintaining the aspect ratio.
- Pads images to match the reference image's width.
- Supports common image formats including JPG, JPEG, PNG, BMP, and GIF.
- Users can specify paths either through command line arguments or a JSON configuration file.

## Getting Started

### Prerequisites
- Python 3.x
- Pillow library (PIL fork), can be installed via pip:
  pip install Pillow

### Installation
Clone the repository using:
  git clone https://github.com/<your-username>/ImageResizer.git

### Usage

#### Using Command Line Arguments
Run the script with the paths as arguments:
  python image_resizer.py --input_dir <path-to-input-dir> --output_dir <path-to-output-dir> --ref_image <path-to-reference-image>

#### Using a Configuration File
Create a JSON file (e.g., config.json) with the following structure:
{
    "input_dir": "<path-to-input-dir>",
    "output_dir": "<path-to-output-dir>",
    "ref_image": "<path-to-reference-image>"
}
Run the script with the config file:
  python image_resizer.py --config <path-to-config-file>

## Contributing
Contributions to enhance the script are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.

## Contact
For any queries or contributions, please open an issue in the GitHub repository.
