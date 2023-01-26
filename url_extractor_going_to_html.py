#import requests_html 
import re
import continue_scrolling
import os
import sys
def noduplicate(items): 
    unique = [] 
    for item in items: 
        if item not in unique: 
            unique.append(item)
    return unique 

def openfile():
	
    try:
        with open(log_file, 'r') as file_obj:
            complete_content = file_obj.read()
    except Exception:
        print("error") 
def results(datamode,linksmode):
    #try:
    with open("data.txt", datamode) as data:
        with open("links.txt", linksmode) as links:
            if data.read()=="missing":
                print("missing")
                return links
            if data.read()=="full":
                print("full")
                return "nothingtoadd"
                    
    #except Exception:
        #print("error")

def extractor(url):
    #print("extractor works")
    #print(url)
    with open(os.path.join(sys.path[0], "links.txt"), "r") as f:
        video_ids = f.readlines()
    if results("r","r")=="nothingtoadd": return video_ids
    playlist_lenght=0
    #html = requests_html.HTMLSession().get(url).html.absolute_links
    html = continue_scrolling.scrolling(url)
    print(html)
    print(html)
    while playlist_lenght<5:
        #html = urllib.request.urlopen(url)
        video_ids =video_ids + re.findall(r"watch\?v=(\S{11})", str(html))
        video_ids = noduplicate(video_ids)
        playlist_lenght=len(video_ids)
        html = continue_scrolling.more_scroll()
        print(html,"source")
        print(len(video_ids))
    #links = open("links.txt", "w").writelines(video_ids).close()
    #data = open("data.txt", "w").write("full").close()
    return video_ids
    print(str("there are %d videos" %len(video_ids)))
