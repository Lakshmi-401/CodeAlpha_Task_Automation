import os
import shutil
import re

# CodeAlpha - Task 3: Task Automation

def move_jpg_files(source_folder, destination_folder):
    """Moves all .jpg files from source to destination"""
    
    # Create destination if not exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created folder: {destination_folder}")

    count = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
            source_path = os.path.join(source_folder, file)
            dest_path = os.path.join(destination_folder, file)
            shutil.move(source_path, dest_path)
            print(f"Moved: {file}")
            count += 1
    
    if count == 0:
        print("No .jpg files found in source folder.")
    else:
        print(f"\nSuccessfully moved {count} files!")

def extract_emails(file_path):
    """Extracts emails from a text file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Regex for emails
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
    
    print(f"Found {len(emails)} emails:")
    for email in emails:
        print(email)
    return emails

# MAIN
if __name__ == "__main__":
    print("=== CodeAlpha Task Automation ===")
    print("1. Move JPG Files")
    print("2. Extract Emails from File")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        src = input("Enter source folder path (e.g., ./source): ")
        dest = input("Enter destination folder path (e.g., ./destination): ")
        move_jpg_files(src, dest)
    elif choice == '2':
        path = input("Enter text file path: ")
        extract_emails(path)
    else:
        print("Demo run with default folders...")
        move_jpg_files("test_source", "test_destination")
