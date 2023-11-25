# Modified version of my script for cross-platform use.
# Pat Findley 17 Apr 2021
# converted for pi and magic mirror 20 Nov 23
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# browser.cache.memory.limit < - set to something realistic or it will eat all your rams.
# Double-click the browser.sessionstore.resume_from_crash to switch it from true to false.
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
import os
import pyautogui


#time.sleep(30)
#os.system('/usr/bin/firefox-esr -kiosk &')


site66 = ["http://magicmirror.findley.cc:8080", 120] #Magic Mirror
site67 = ["http://magicmirror.findley.cc:8081", 120] #Magic Mirror2
site68 = ["http://magicmirror.findley.cc:8082", 120] #Magic Mirror3
site69 = ["http://magicmirror.findley.cc:8083", 120] #Magic Mirror4
site70 = ["http://magicmirror.findley.cc:8084", 120] #Magic Mirror5
site72 = ["http://en.blitzortung.org/live_lightning_maps.php?map=30", 120]
site73 = ["https://www.nhc.noaa.gov", 60]
site74 = ["https://www.mlb.com/postseason", 60]
site75 = ["https://merrysky.net/forecast/olivette,%20mo/us", 120] #merry sky for STL


websites = [site66, site68, site69, site70, site72]

usebrowser = webbrowser.get('Firefox')
#usebrowser.open('--kiosk initialsite[0]')
#pyautogui.hotkey('alt','tab')
#pyautogui.press('F11')

VAR_CYCLE = 1
F11_CYCLE = 0
while VAR_CYCLE > 0:
   for website in websites:
      usebrowser.open(website[0], new=0)
      if F11_CYCLE < 1:
         pyautogui.press('F11')
         F11_CYCLE = 1
      time.sleep(website[1])