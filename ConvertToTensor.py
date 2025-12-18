import os
import torch
from sentence_transformers import SentenceTransformer

def text_to_tensor_and_save(folder_path):
    """Convert text files to tensors and save them in the same text files."""
    # Load the model
    model = SentenceTransformer("l3cube-pune/telugu-sentence-similarity-sbert")
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                # Read the content of the text file
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read().strip()
                
                # Convert the text content to a tensor
                tensor = model.encode([content], convert_to_tensor=True)
                
                # Convert tensor to string representation
                tensor_str = tensor[0].cpu().numpy().tolist()
                
                # Save the tensor string representation back to the text file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(str(tensor_str))
                
                print(f"Converted {file_path} content to tensor and saved back to the file")
            except Exception as e:
                print(f"Failed to convert {file_path} to tensor: {e}")

if __name__ == "__main__":
    # Specify the path to the folder containing the text files
    folder_path = "/Users/rohithpallamreddy/Documents/Audios/transcriptions"
    text_to_tensor_and_save(folder_path)
