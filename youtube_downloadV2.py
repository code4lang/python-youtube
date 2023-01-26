#https://www.youtube.com/playlist?list=PLGt8Zwk3Khs0ddNEzlbmXtzW5fczTsMuZ
from  tkinter import *
#from pytube import YouTube 
#from pytube import Playlist
import yt_dlp
import url_extractor_going_to_html


root=Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")



Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()




##enter link
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader(a):
    print("dowloader works")
    video_url=str(a)
    video_info = yt_dlp.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
    print("Download complete... {}".format(filename))

def playlist_download():
    global url
    error=[]
    url=url_extractor_going_to_html.extractor(link.get())
    for vid in url:
        try:
            Downloader(vid)
        except Exception:
            error.append(vid)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = playlist_download).place(x=180 ,y = 150)



root.mainloop()
while 1:
    continue
