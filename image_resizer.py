import os
import argparse
import json
from PIL import Image, ImageOps

def resize_and_pad_images(input_dir, output_dir, ref_image_path):
    # Load the reference image to get the correct size
    ref_image = Image.open(ref_image_path)
    ref_width, ref_height = ref_image.size

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each image in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # check for image files
            img_path = os.path.join(input_dir, file_name)
            img = Image.open(img_path)

            # Calculate the scale factor to match the reference height while keeping aspect ratio
            scale_factor = ref_height / img.size[1]
            new_size = (int(img.size[0] * scale_factor), ref_height)

            # Resize the image
            img_resized = img.resize(new_size, Image.Resampling.LANCZOS)

            # Determine padding to add to match reference width
            pad_width = ref_width - new_size[0]
            left_pad = pad_width // 2
            right_pad = pad_width - left_pad

            # Add padding
            img_padded = Image.new('RGB', (ref_width, ref_height), (255, 255, 255))
            img_padded.paste(img_resized, (left_pad, 0))

            # Save the processed image to the output directory
            output_path = os.path.join(output_dir, file_name)
            img_padded.save(output_path)

def main():
    parser = argparse.ArgumentParser(description='Resize and pad images to match a reference image.')
    parser.add_argument('--input_dir', help='Path to the input directory', required=False)
    parser.add_argument('--output_dir', help='Path to the output directory', required=False)
    parser.add_argument('--ref_image', help='Path to the reference image', required=False)
    parser.add_argument('--config', help='Path to the configuration JSON file', required=False)

    args = parser.parse_args()

    if args.config:
        with open(args.config, 'r') as config_file:
            config = json.load(config_file)
            input_dir = config['input_dir']
            output_dir = config['output_dir']
            ref_image_path = config['ref_image']
    else:
        input_dir = args.input_dir or input("Enter the path to the input directory: ")
        output_dir = args.output_dir or input("Enter the path to the output directory: ")
        ref_image_path = args.ref_image or input("Enter the path to the reference image: ")

    resize_and_pad_images(input_dir, output_dir, ref_image_path)

if __name__ == "__main__":
    main()
