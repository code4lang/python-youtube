import youtube_dl
url='https://youtube.com/playlist?list=PL-5DqpOAMXS9s45uqqU4mYLKwLNHpnDCK'
ydl = youtube_dl.YoutubeDL({'url': url,
                            'download' : 'False'})

playlist=ydl.extract_info(url, download=False)
'''for video in playlist['entries']:
    print(str(video['url'])) '''
import os
play_urls=os.system('youtube-dl --get-id url -i')
print(dir(play_urls))
#for video in play_urls['entries']:
 #   print(str(video['url']))
