# **File Organizer Python Tool**

This Python script automates the organization of files in a specified directory. It categorizes files based on their extensions into folders like **"Documents"**, **"Images"**, **"Videos"**, and **"Others"**.

## **Features**:
- Organizes files into folders based on file type.
- Supports document, image, and video file extensions.
- Automatically creates necessary directories if they do not exist.
- Handles common file extensions like `.txt`, `.jpg`, `.mp4`, and more.

---

## **How It Works**:

1. **Input Directory**:  
   When prompted, enter the **full path** of the directory you want to organize.

2. **File Sorting**:  
   The script will create four folders in the directory if they do not already exist:  
   - **Documents**: `.txt`, `.doc`, `.docx`, `.pdf`
   - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`
   - **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`
   - **Others**: Files with extensions not recognized as document, image, or video will be moved to the **Others** folder.

---



## **Demo**:

![Demo GIF](File_Organizer_Demo.gif)

---
## **Customization**:


- **File Extensions**:  
  You can customize the extensions recognized by editing the lists of `document_extensions`, `image_extensions`, and `video_extensions` in the script.

- **Folders**:  
  The script currently creates **4 folders** (**Documents**, **Images**, **Videos**, **Others**), but you can add more categories if desired by modifying the logic in the `get_folder_by_extension` method.


---

Good luck with your file organization, and **Happy organizing!** ✨
