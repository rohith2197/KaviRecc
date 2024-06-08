import os
import wave
import contextlib
import math
import time
import subprocess
import speech_recognition as sr
from pydub import AudioSegment


def convert_audio_format(input_path, output_path, output_format="wav"):
    """Convert audio file to the specified format using pydub."""
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format=output_format)
        print(f"Converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Failed to convert {input_path}: {e}")
        
def extract_audio(video_path, audio_path):
    """Extract audio from a video file using ffmpeg."""
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
    """Split audio file into segments of a specified length (in seconds)."""
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

def transcribe_audio(audio_path, retries=3, delay=5):
    """Transcribe the audio file to text with retries for connection errors."""
    r = sr.Recognizer()
    for attempt in range(retries):
        try:
            with sr.AudioFile(audio_path) as source:
                audio_data = r.record(source)
            text = r.recognize_google(audio_data, language='te-IN')
            return text
        except sr.UnknownValueError:
            return "[Unrecognized audio]"
        except sr.RequestError as e:
            print(f"Request error: {e}. Retrying ({attempt + 1}/{retries})...")
            time.sleep(delay)
    return "[Failed to transcribe due to request error]"

def transcribe_audio_segments(segment_paths):
    """Transcribe each audio segment and combine the transcriptions."""
    transcriptions = []
    for i, segment_path in enumerate(segment_paths):
        print(f"Transcribing segment {i + 1}/{len(segment_paths)}...")
        text = transcribe_audio(segment_path)
        transcriptions.append(text)
    return " ".join(transcriptions)

def process_audio_files(folder_path, segment_length=60):
    # Create an output folder for transcriptions
    output_folder = os.path.join(folder_path, "transcriptions")
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith((".wav", ".mp3", ".m4a")):
            input_path = os.path.join(folder_path, filename)
            # Convert audio file to WAV format if necessary
            if not filename.endswith(".wav"):
                wav_path = os.path.splitext(input_path)[0] + ".wav"
                convert_audio_format(input_path, wav_path)
            else:
                wav_path = input_path
            
            # Split the audio into segments and transcribe each segment
            segment_paths = split_audio(wav_path, segment_length)
            transcription = transcribe_audio_segments(segment_paths)
            
            # Save the transcription to a text file
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_folder, output_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(transcription)
            print(f"Saved transcription to {output_path}")

if __name__ == "__main__":
    # Specify the path to the folder containing the audio files
    folder_path = "/Users/rohithpallamreddy/Documents/Audios"
    process_audio_files(folder_path)
