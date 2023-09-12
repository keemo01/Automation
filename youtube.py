# Import necessary libraries
import os  # Import the os library for file and folder operations
from pytube import YouTube  # Import the YouTube class from the pytube library
from pathlib import Path  # Import the Path class from the pathlib library

# Define a function to download a YouTube video
def download_youtube_video(video_url, download_folder):
    try:
        # Ensure the download folder exists
        download_path = Path(download_folder)  # Create a Path object for the download folder path
        download_path.mkdir(parents=True, exist_ok=True)  # Create the folder if it doesn't exist

        # Initialize a YouTube object
        yt = YouTube(video_url)  # Create a YouTube object using the provided video URL

        # Select the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()  # Choose the best video quality available

        # Download the video to the specified folder
        video_stream.download(output_path=download_path)  # Download the video and save it to the folder

        # Get the title of the downloaded video
        video_title = yt.title  # Retrieve the title of the video

        # Return the video title and the full path to the downloaded video file
        return video_title, download_path / f"{video_title}.mp4"
    except Exception as e:
        # Handle any exceptions that may occur during the download process
        return None, str(e)  # Return None and the error message if an error occurs

# Entry point of the script
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=PG2GLkqeMYM&t=12s"  # URL of the YouTube video to download
    download_folder = "/Users/Ajoko/Documents/video"  # Folder where the video will be saved

    # Call the download_youtube_video function and store the returned values
    video_title, video_path = download_youtube_video(video_url, download_folder)

    # Check if the download was successful
    if video_title and video_path:
        print(f"Video downloaded to {video_path}")  # Print a success message with the download path
    else:
        print("An error occurred while downloading the video.")  # Print an error message if download fails
