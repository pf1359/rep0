# Modified version of my script for cross-platform use.
# Pat Findley 17 Apr 2021
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

#########
# Determine platform and define Firefox instead of using default
import platform
hostplatform = platform.system()
if hostplatform =='Windows':
    webbrowser.register('Firefox',
	   None,
	   webbrowser.BackgroundBrowser("C://Program Files//Mozilla Firefox//firefox.exe"))

usebrowser = webbrowser.get('Firefox')

site07 = ["https://ncov2019.live/", 60]
site08 = ["https://ncov2019.live/data/unitedstates", 60]
site35 = ["https://coinmarketcap.com/watchlist", 180]
site36 = ["http://wttr.in/Saint+Louis+Missouri", 120]
site38 = ["http://www.internettrafficreport.com/", 120]
site39 = ["https://cybermap.kaspersky.com", 120]
site40 = ["https://www.akamai.com/us/en/resources/visualizing-akamai/enterprise-threat-monitor.jsp", 120]
site41 = ["https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6", 120]
site42 = ["https://map.internetintel.oracle.com/?root=national&country=US", 120]
site43 = ["https://threatmap.checkpoint.com/", 120]
site44 = ["https://threatbutt.com/map/", 120]
site45 = ["https://securitycenter.sonicwall.com/m/page/worldwide-attacks", 120]



websites = [site07, site08, site35, site36, site38, \
    site39, site40, site41, site42, site43, site44, site45]

VAR_CYCLE = 1
while VAR_CYCLE > 0:
   for website in websites:
      usebrowser.open(website[0], new=0)
      time.sleep(website[1])

