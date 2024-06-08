import os
from moviepy.editor import VideoFileClip

def convert_videos_to_audio(folder_path, audio_format="mp3"):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Create an output folder for audio files
    output_folder = os.path.join(folder_path, "audio_files")
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a video file
        if filename.endswith((".mp4", ".avi", ".mov", ".mkv")):
            file_path = os.path.join(folder_path, filename)
            try:
                # Load the video file
                video = VideoFileClip(file_path)
                
                # Extract the audio
                audio = video.audio
                
                # Define the audio file path
                audio_filename = os.path.splitext(filename)[0] + f".{audio_format}"
                audio_path = os.path.join(output_folder, audio_filename)
                
                # Write the audio file
                audio.write_audiofile(audio_path)
                
                print(f"Converted {filename} to {audio_filename}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    # Specify the path to the folder containing the video files
    folder_path = r"/Users/rohithpallamreddy/Documents/TeluguAudioShowsDownloaded"
    convert_videos_to_audio(folder_path)
