from sentence_transformers import SentenceTransformer
import torch
import subprocess
import os
import math
import wave
import contextlib
import speech_recognition as sr
from pytube import YouTube
import os

def remove_mp4_files():
    # Get the current working directory
    cwd = os.getcwd()
    
    # Iterate over all files in the directory
    for filename in os.listdir(cwd):
        # Check if the file ends with .mp4
        if filename.endswith('.mp4') or filename.endswith('.wav'):
            # Construct the full file path
            file_path = os.path.join(cwd, filename)
            # Remove the file
            os.remove(file_path)
            print(f"Removed: {file_path}")

def extract_audio(video_path, audio_path):
    try:
        command = [
            "ffmpeg",
            "-i", video_path,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "44100",
            "-ac", "2",
            audio_path
        ]
        subprocess.run(command, check=True)
        print("Audio extraction complete")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while extracting audio: {e}")

def split_audio(audio_path, segment_length):
    with contextlib.closing(wave.open(audio_path, 'rb')) as f:
        frame_rate = f.getframerate()
        n_frames = f.getnframes()
        duration = n_frames / frame_rate

    segment_paths = []
    for i in range(math.ceil(duration / segment_length)):
        start_time = i * segment_length
        segment_path = f"{os.path.splitext(audio_path)[0]}_segment_{i}.wav"
        command = [
            "ffmpeg",
            "-i", audio_path,
            "-ss", str(start_time),
            "-t", str(segment_length),
            "-acodec", "copy",
            segment_path
        ]
        subprocess.run(command, check=True)
        segment_paths.append(segment_path)
    
    return segment_paths

def transcribe_audio(audio_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data, language='te-IN')
        return text
    except sr.UnknownValueError:
        return "[Unrecognized audio]"
    except sr.RequestError as e:
        return f"[Request error: {e}]"

def transcribe_audio_segments(segment_paths):
    transcriptions = []
    for i, segment_path in enumerate(segment_paths):
        print(f"Transcribing segment {i + 1}/{len(segment_paths)}...")
        text = transcribe_audio(segment_path)
        transcriptions.append(text)
    return " ".join(transcriptions)

def transcribe_video(video_path, segment_length=60):
    # Generate a temporary path for the audio file
    audio_path = f"{os.path.splitext(video_path)[0]}.wav"
    
    # Extract audio from the video
    extract_audio(video_path, audio_path)
    
    # Split the audio into segments and transcribe each segment
    segment_paths = split_audio(audio_path, segment_length)
    transcription = transcribe_audio_segments(segment_paths)
    
    # Clean up the temporary audio and segment files
    os.remove(audio_path)
    for segment_path in segment_paths:
        os.remove(segment_path)
    
    return transcription

model = SentenceTransformer("l3cube-pune/telugu-sentence-bert-nli")

def remove_words(text, word="[Unrecognized audio]"):
    cleaned_content = text.replace(word, "")
    return cleaned_content

def convert_to_tensor(text):
    return model.encode([text], convert_to_tensor=True)

def compare_two(first, second):
    similarity = torch.nn.functional.cosine_similarity(first, second)
    return similarity.item()  # Convert tensor to a float

def download_youtube_video(url, download_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video and get the file path
        file_path = stream.download(output_path=download_path)
        
        # Return the file path
        return file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def compare_links(first, second):
    first_tensor = convert_to_tensor(remove_words(transcribe_video(download_youtube_video(first))))
    second_tensor = convert_to_tensor(remove_words(transcribe_video(download_youtube_video(second))))
    return compare_two(first_tensor, second_tensor)

print(compare_links(input("Enter your first link: "), input("Enter your second link: ")))
remove_mp4_files()