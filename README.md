# ImageResizer
A Python script that resizes and pads images to match the dimensions of a reference image. This is particularly useful for standardizing the size of a batch of images.

## Features

- Resizes images to match the height of a reference image while maintaining the aspect ratio.
- Adds padding to images to match the width of the reference image.
- Supports common image formats including JPG, JPEG, PNG, BMP, and GIF.

## Getting Started

### Prerequisites

- Python 3.x
- Pillow library (PIL fork), install via pip: `pip install Pillow`

### Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/ImageResizer.git
Usage
Place the images you want to resize in the Input_files directory.
Specify the path of the reference image in image_resizer.py.
Run the script:
bash

python image_resizer.py
The resized images will be saved in the output_files directory.
Contributing

Contributions to improve the script are welcome. Please feel free to fork the repository and submit a pull request.

License

This project is licensed under the MIT License - see the LICENSE.md file for details.
