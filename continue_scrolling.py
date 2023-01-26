from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
bot = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

def scrolling(url):
    #print("scrolling works")
    
    
    #url = 'https://www.youtube.com/playlist?list=PLGt8Zwk3Khs0ddNEzlbmXtzW5fczTsMuZ'
    bot.get(url)
    
    #waiting for the page to load
    time.sleep(1) 
    #repeat scrolling 10 times

    return more_scroll()
def more_scroll():
    for i in range(10):
        #scroll 300 px
        bot.execute_script('window.scrollTo(0,(window.pageYOffset+3000))')
        #waiting for the page to load
        time.sleep(1) 
    html=bot.page_source
   
    return html
