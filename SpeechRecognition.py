import subprocess
import os
import math
import wave
import contextlib
import speech_recognition as sr

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

# Paths and settings
video_path = "/Users/rohithpallamreddy/Documents/amplify/4 Minutes 24 Headlines  8 AM  30-05-2024 - TV9.mp4"
audio_path = "/Users/rohithpallamreddy/Documents/amplify/Amrutham_Serial_Ep_197.wav"
segment_length = 60  # seconds

# Extract audio from the video
extract_audio(video_path, audio_path)

# Split the audio into segments and transcribe each segment
segment_paths = split_audio(audio_path, segment_length)
transcriptions = transcribe_audio_segments(segment_paths)
print("Transcription:", transcriptions)
