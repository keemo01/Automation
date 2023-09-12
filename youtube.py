import os
from pytube import YouTube
from pathlib import Path

def download_youtube_video(video_url, download_folder):
    try:
        # Ensure the download folder exists
        download_path = Path(download_folder)
        download_path.mkdir(parents=True, exist_ok=True)

        # Initialize a YouTube object
        yt = YouTube(video_url)

        # Select the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified folder
        video_stream.download(output_path=download_path)

        # Get the title of the downloaded video
        video_title = yt.title

        return video_title, download_path / f"{video_title}.mp4"
    except Exception as e:
        return None, str(e)

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=PG2GLkqeMYM&t=12s"
    download_folder = "/Users/Ajoko/Documents/video"

    video_title, video_path = download_youtube_video(video_url, download_folder)

    if video_title and video_path:
        print(f"Video downloaded to {video_path}")
    else:
        print("An error occurred while downloading the video.")
