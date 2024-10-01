import yt_dlp
from sys import argv

link = argv[1]

ydl_opts = {
    'format': 'best',
    'outtmpl': r'C:\Users\Victory\Videos\YtDownloader\%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
