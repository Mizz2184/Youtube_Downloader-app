import streamlit as st
from pytube import YouTube


def download_video(url):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the highest resolution stream
        stream = video.streams.get_highest_resolution()

        # Download the video
        stream.download()

        st.success("Video downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


# Streamlit GUI code
st.title("YouTube Video Downloader")

# Get the video URL from the user
video_url = st.text_input("Enter the YouTube video URL:")

# Download button
if st.button("Download"):
    if video_url:
        st.info("Downloading video...")
        download_video(video_url)
    else:
        st.warning("Please enter a valid YouTube video URL.")
