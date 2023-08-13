# Modified version of my script for cross-platform use.
# Pat Findley 17 Apr 2021
# Copied to picycle on 13 Aug 2023 for raspberry pi
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# browser.cache.memory.limit < - set to something realistic or it will eat all your rams.
# Remember to go into options and enable autoplay audio and video if using Youtube links
    #from selenium import webdriver
    #driver = webdriver.Chrome()
    #driver.get(link1)
#import random

#All this is commented out and it uses the default browser.
#Opening in the same tab only works in Firefox (new=0), and only if you make the changes above.
#firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe %s"
#webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
#IF Linux, we need this and change webbrowser.open to firefox.open
#firefox = webbrowser.get('Firefox')

import webbrowser
import time
from selenium import webdriver

#########
# Determine platform and define Firefox instead of using default
import platform
hostplatform = platform.system()
if hostplatform =='Windows':
    webbrowser.register('Firefox',
	   None,
	   webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))
    
f = webdriver.Firefox()
f.get('http://magicmirror.findley.cc:8080')
f.fullscreen_window()

usebrowser = webbrowser.get('Firefox')

site01 = ["http://magicmirror.findley.cc:8080", 240]
site02 = ["https://www.pollen.com/forecast/current/pollen/63132", 30]
#site04 = Wunderground US Radar
site04 = ["https://www.wunderground.com/wundermap?lat=37.7&lon=-92.7&zoom=4&radar=1&wxstn=0", 60]
site05 = ["http://en.blitzortung.org/live_lightning_maps.php?map=30", 60]
site06 = ["https://radar.weather.gov/?settings=v1_eyJhZ2VuZGEiOnsiaWQiOiJ3ZWF0aGVyIiwiY2VudGVyIjpbLTkwLjIsMzguNjI4XSwiem9vbSI6NywibG9jYXRpb24iOlstOTAuMiwzOC42MjhdfSwiYmFzZSI6InN0YW5kYXJkIiwiY291bnR5IjpmYWxzZSwiY3dhIjpmYWxzZSwic3RhdGUiOmZhbHNlLCJtZW51Ijp0cnVlLCJzaG9ydEZ1c2VkT25seSI6ZmFsc2V9#/", 120]
#site06 = wunderground temp readings
site07 = ["https://www.wunderground.com/wundermap", 60]
site08 = ["https://www.wunderground.com/dashboard/pws/KMOSTLOU477", 60]

websites = [site01, site02, site04, site05, site06, site07, site08]

VAR_CYCLE = 1
while VAR_CYCLE > 0:
   for website in websites:
      usebrowser.open(website[0], new=0)
      time.sleep(website[1])

