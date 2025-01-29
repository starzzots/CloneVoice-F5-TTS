import tarfile
import os

# Define the path to the tar.bz2 file and the extraction directory
file_path = r"C:\Users\Kyle\Documents\Awillremove\LJSpeech-1.1.tar.bz2"
extraction_dir = r"C:\Users\Kyle\Documents\Awillremove"

# Open the tar.bz2 file
with tarfile.open(file_path, "r:bz2") as tar:
    # Extract all contents to the specified directory
    tar.extractall(path=extraction_dir)
    print(f"Extracted all files to: {extraction_dir}")
 