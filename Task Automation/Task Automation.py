import os
import shutil

# Define the source directory
source_dir = 'Downloads'

# Define the target directories
target_dirs = {
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'Documents': ['pdf', 'docx', 'txt', 'xlsx'],
    'Audio': ['mp3', 'wav', 'flac'],
    'Video': ['mp4', 'avi', 'mkv'],
    'Others': []  # For any other file types
}

# Create target directories if they do not exist
for dir_name in target_dirs.keys():
    os.makedirs(os.path.join(source_dir, dir_name), exist_ok=True)

# Function to get the file extension
def get_file_extension(file_name):
    return file_name.split('.')[-1].lower()

# Function to move files
def move_files():
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        if os.path.isfile(file_path):
            file_ext = get_file_extension(file_name)
            moved = False
            for dir_name, extensions in target_dirs.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(source_dir, dir_name, file_name))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(source_dir, 'Others', file_name))

# Run the file organization script
if __name__ == "__main__":
    move_files()
    print("Files have been organized successfully!")
