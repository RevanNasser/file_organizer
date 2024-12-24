import os
import shutil

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory

    def organize_files(self):
        # Create folders if not exists
        folders = ['Documents', 'Images', 'Videos', 'Others']
        for folder in folders:
            folder_path = os.path.join(self.directory, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

        # Organize files based on their extensions
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)

            if os.path.isfile(file_path):
                # Extract file extension by splitting on the dot and checking if it's valid
                file_extension = self.get_file_extension(filename)
                if file_extension:
                    file_extension = file_extension.lower()  # Convert to lowercase for consistency
                    destination_folder = self.get_folder_by_extension(file_extension)

                    if destination_folder:
                        destination_path = os.path.join(self.directory, destination_folder, filename)
                        shutil.move(file_path, destination_path)
                else:
                    print(f"Skipping file '{filename}' (no valid extension found).")

    def get_file_extension(self, filename):
        # Get the file extension by splitting at the last dot
        name_parts = filename.rsplit('.', 1)
        if len(name_parts) > 1:
            return name_parts[1]
        return None

    def get_folder_by_extension(self, file_extension):
        document_extensions = ['txt', 'doc', 'docx', 'pdf']
        image_extensions = ['jpg', 'jpeg', 'png', 'gif']
        video_extensions = ['mp4', 'mov', 'avi', 'mkv']

        if file_extension in document_extensions:
            return 'Documents'
        elif file_extension in image_extensions:
            return 'Images'
        elif file_extension in video_extensions:
            return 'Videos'
        else:
            return 'Others'

def organize_files_in_directory(directory_to_organize):
    if os.path.exists(directory_to_organize) and os.path.isdir(directory_to_organize):
        organizer = FileOrganizer(directory_to_organize)
        organizer.organize_files()
        print("Files organized successfully!")
    else:
        print("Invalid directory path. Please provide a valid directory.")

directory_path = input("Enter the directory path to organize: ").strip()
print(f"Provided directory path: {directory_path}")
organize_files_in_directory(directory_path)
