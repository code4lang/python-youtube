from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#bot = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
bot = webdriver.Chrome(options=options)

def bypass_popup(bot):
    WebDriverWait(bot, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="uc-btn-accept-banner"]'))).click()
    '''consent_button_xpath = "//button[@aria-label='Agree to the use of cookies and other data for the purposes described']"
    consent = WebDriverWait(bot, 10).until(EC.element_to_be_clickable(
        (By.XPATH, consent_button_xpath)))

    consent = bot.find_element_by_xpath(consent_button_xpath)
    consent.click()'''

def scrolling(url):
    #print("scrolling works")
    
    
    #url = 'https://www.youtube.com/playlist?list=PLGt8Zwk3Khs0ddNEzlbmXtzW5fczTsMuZ'
    bot.get(url)
    bypass_popup(bot)
    #waiting for the page to load
    time.sleep(4)
    
 
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
