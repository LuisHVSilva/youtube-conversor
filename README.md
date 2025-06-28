# 🎥 yt-resilient-downloader

A robust and fail-safe YouTube video downloader built with Python, combining the simplicity of `pytube` with the power and reliability of `yt-dlp` as an automatic fallback mechanism.

---

## 🚀 Features

- ✅ **Primary engine:** Downloads `.mp4` videos using `pytube` (lightweight and simple).
- 🔁 **Fallback to `yt-dlp`:** If `pytube` fails due to API or structure changes (e.g., HTTP 400), `yt-dlp` takes over automatically.
- 🔍 **Smart detection:** Ignores playlist/mix links when fallback is triggered.
- 🧠 **Best resolution:** Downloads the highest available progressive video with embedded audio.
- 📂 **Custom output path:** Saves files in a configurable local directory.
- 💼 **Clean, production-ready codebase** with clear structure and error handling.

---

## 🧰 Requirements

```bash
pip install pytube yt-dlp
```


##💡 Usage
```bash
from downloader import download_youtube_video

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
download_youtube_video(url, output_path='./videos')
```

The downloader will:
1. - Try using pytube first.
2. - If it fails, it will automatically switch to yt-dlp with playlist detection disabled.

## 📁 File Structure
yt-resilient-downloader/
├── downloader.py        # Main logic: pytube + yt-dlp fallback
├── main.py              # Example usage
├── README.md
└── requirements.txt     # Dependency list

## 🧪 Sample Output

```bash
[PyTube] Downloading: Video Title
[PyTube] Download completed at: ./videos

or (on failure):

[PyTube] Failed: HTTP Error 400
[yt-dlp] Attempting download...
[yt-dlp] Download completed at: ./videos
```

## 🛑 Notes & Legal Disclaimer
This tool is for educational and personal use only.
You are solely responsible for how you use it.
Downloading copyrighted material without permission may violate YouTube’s Terms of Service.


## 📜 License
This project is released under the MIT License.

## 🤝 Contributing
Pull requests and suggestions are welcome! Open an issue or fork the repo to get started.
