import os

def clean_transcriptions(folder_path, target_text="[Unrecognized audio]"):
    """Remove specific target text from all text files in a directory."""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                # Read the content of the text file
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                # Remove the target text
                cleaned_content = content.replace(target_text, "")
                
                # Save the cleaned content back to the file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(cleaned_content)
                
                print(f"Cleaned {file_path}")
            except Exception as e:
                print(f"Failed to clean {file_path}: {e}")

if __name__ == "__main__":
    # Specify the path to the folder containing the text files
    folder_path = "/Users/rohithpallamreddy/Documents/Audios/transcriptions"
    clean_transcriptions(folder_path)
