from pytube import YouTube

def download_youtube_video(url, download_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()
        
        # Download the video
        print(f"Downloading {yt.title}...")
        stream.download(output_path=download_path)
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the YouTube video to download
# video_url = 'https://www.youtube.com/watch?v=_rKlc8k0b50'

# Path where you want to save the downloaded video
download_path = r"/Users/rohithpallamreddy/Documents/TeluguAudioShowsDownloaded"

# Call the function to download the video
while(True):
    video_url = input()
    download_youtube_video(video_url, download_path)
