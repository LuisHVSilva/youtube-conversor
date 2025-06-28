import os
from pytube import YouTube
import yt_dlp


def download_with_pytube(url, output_path='.'):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')\
                           .order_by('resolution').desc().first()
        print(f'[PyTube] Downloading: {yt.title}')
        stream.download(output_path=output_path)
        print(f'[PyTube] Download completed at: {output_path}')
        return True
    except Exception as e:
        print(f'[PyTube] Failed: {e}')
        return False


def download_with_ytdlp(url, output_path='.'):
    try:
        print(f'[yt-dlp] Attempting download...')
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f'[yt-dlp] Download completed at: {output_path}')
    except Exception as e:
        print(f'[yt-dlp] Failed: {e}')


def download_youtube_video(url, output_path='./videos'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if not download_with_pytube(url, output_path):
        print('[Info] Falling back to yt-dlp...')
        download_with_ytdlp(url, output_path)


# ==== Example usage ====
if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=iDD2Gpu9BdQ'
    download_youtube_video(video_url)
