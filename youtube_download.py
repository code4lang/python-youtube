#https://www.youtube.com/playlist?list=PLGt8Zwk3Khs0ddNEzlbmXtzW5fczTsMuZ
from  tkinter import *
from pytube import YouTube 
from pytube import Playlist
import youtube_dl
import url_extractor_going_to_html
from memory_profiler import profile


root = Tk()

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
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
    print("Download complete... {}".format(filename))

start=0
def starter():
	start=1
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = starter).place(x=180 ,y = 150)

root.mainloop()
def playlist_download():
    global url
    url=url_extractor_going_to_html.extractor(link.get())
    for vid in url:
        Downloader(vid)
while 1:
    if start==1: playlist_download
    continue
