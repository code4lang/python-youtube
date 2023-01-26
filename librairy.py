from pytube import *
from tkinter import *


#display window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("youtube playlist audio downloader")

#widget in the window
Label(root,text = 'Youtube playlist audio Downloader', font ='arial 20 bold').pack()

#Create Field to Enter Link
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
p = Playlist(str(link))
links=p.video_urls
for url in links[:3]:
    print(url)



root.mainloop()
#https://youtube.com/playlist?list=PL-5DqpOAMXS9s45uqqU4mYLKwLNHpnDCK
