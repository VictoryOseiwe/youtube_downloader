# YouTube Video Downloader

A simple Python script to download YouTube videos using the `yt-dlp` library. This tool downloads the highest available quality of a video and saves it to your local machine.

## Features
- Downloads YouTube videos in the best available quality.
- Saves the video with its title as the filename.
- Easy command-line usage with minimal setup.
- Downloads directly to a specified directory (`C:\Users\Victory\Videos\YtDownloader`).

## Requirements
- Python 3.6+
- `yt-dlp` Python library

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/youtube-video-downloader.git
    cd youtube-video-downloader
    ```

2. **Install the Required Dependencies**:
    Install `yt-dlp` using pip:
    ```bash
    pip install yt-dlp
    ```

## Usage

1. **Run the Script**:
   Provide the YouTube video URL as a command-line argument:
   ```bash
   python youtube_downloader.py "https://www.youtube.com/watch?v=example"
