# Modified version of my script for cross-platform use.
# Pat Findley 17 Apr 2021
# converted for pi and magic mirror 20-24 Nov 23
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# browser.cache.memory.limit < - set to something realistic or it will eat all your rams.
# Double-click the browser.sessionstore.resume_from_crash to switch it from true to false.
# Create a launch.sh in mm home that launches firefox-esr --kiosk, then this script


import webbrowser
import time


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

VAR_CYCLE = 1
while VAR_CYCLE > 0:
   for website in websites:
      usebrowser.open(website[0], new=0)
      time.sleep(website[1])