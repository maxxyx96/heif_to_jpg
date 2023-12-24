from PIL import Image
from pillow_heif import register_heif_opener
import os
import shutil

register_heif_opener()

input_folder = "sadformat"
output_folder = "happyformat"

def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print(f"File copied successfully from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error copying file: {str(e)}")

def convert_heic_to_jpeg(heic_path, jpeg_path):
    im = Image.open(input_folder + "/" + heic_path)  # do whatever need with a Pillow image
    im.save(output_folder + "/" + jpeg_path)

# Specify the path to your HEIC file and the desired JPEG output path

for file_path in os.listdir(input_folder):
    #print(file)
    if ".HEIC" in file_path:
        heic_file_path = file_path
        jpeg_output_path = file_path.replace(".HEIC",".jpg")
        print("old: " + heic_file_path + ";;; new: " + jpeg_output_path)
        convert_heic_to_jpeg(heic_file_path, jpeg_output_path)
    elif ".heic" in file_path:
        heic_file_path = file_path
        jpeg_output_path = file_path.replace(".heic",".jpg")
        print("old: " + heic_file_path + ";;; new: " + jpeg_output_path)
        convert_heic_to_jpeg(heic_file_path, jpeg_output_path)
    else:
        copy_file(str(input_folder + "/" + file_path), str(output_folder + "/" + file_path))