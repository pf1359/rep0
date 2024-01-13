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
import subprocess
restart = 1

VAR_CYCLE = 1
while VAR_CYCLE > 0:

   if restart == 24:
      command = 'pkill firefox'
   command = 'firefox-esr --kiosk http://magicmirror.findley.cc:8080 &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(240)
   command = 'kill %1'

   command = 'firefox-esr --kiosk https://www.pollen.com/forecast/current/pollen/63132 &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(30)

   command = 'firefox-esr --kiosk http://en.blitzortung.org/live_lightning_maps.php?map=30 &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(60)

   command = 'firefox-esr --kiosk https://www.wunderground.com/wundermap?lat=37.7&lon=-92.7&zoom=4&radar=1&wxstn=0 &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(60)

   command = 'firefox-esr --kiosk http://magicmirror.findley.cc:8080 &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(210)

   command = 'firefox-esr --kiosk https://radar.weather.gov/?settings=v1_eyJhZ2VuZGEiOnsiaWQiOiJ3ZWF0aGVyIiwiY2VudGV &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(60)

   command = 'firefox-esr --kiosk https://www.wunderground.com/wundermap &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(60)

   command = 'firefox-esr --kiosk https://www.wunderground.com/dashboard/pws/KMOSTLOU477 &'
   process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
   output, error = process.communicate()
   time.sleep(60)
   
   restart += 1