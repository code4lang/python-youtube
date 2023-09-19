#https://www.youtube.com/playlist?list=PLGt8Zwk3Khs0ddNEzlbmXtzW5fczTsMuZ
import yt_dlp
import url_extractor_going_to_html

link = input("Paste Link Here: ")

def Downloader(a):
    video_url = str(a)
    video_info = yt_dlp.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))

def playlist_download():
    global url
    error = []
    url = url_extractor_going_to_html.extractor(link)
    for vid in url:
        try:
            Downloader(vid)
        except Exception:
            error.append(vid)

playlist_download()