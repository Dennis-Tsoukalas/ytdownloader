import yt_dlp

def download_video(link):
    try:
        ydl_opts = {'outtmpl': 'video_download.mp4'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        return "Download completed successfully!"
    except Exception as e:
        return f"An error occurred: {e}"