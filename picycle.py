# Modified version of my script for cross-platform use.
# Pat Findley 17 Apr 2021
# converted for pi and magic mirror 20 Nov 23
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

time.sleep(30)
#usebrowser = webbrowser.get('Firefox')


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



VAR_CYCLE = 1
while VAR_CYCLE > 0:
   for website in websites:
      usebrowser.open(website[0], new=0)
      time.sleep(website[1])



    # choose a random element from a list
    # seed random number generator
    #random.seed()
    #create a chance to determine if a video plays this cycle
    #chance = random.randint(0, 11)
    # prepare a sequence
    #y1_site = ["https://www.youtube.com/embed/SUyDcyHpFhc?mute=1;autoplay=1", 86] #86 seconds flying past galaxies
    #y2_site = ["https://www.youtube.com/embed/6tmbeLTHC_0?start=54&end=174;mute=1;autoplay=1", 120] #120 seconds the sun 1
    #y3_site = ["https://www.youtube.com/embed/6tmbeLTHC_0?start=267&end=387;mute=1;autoplay=1", 120] #120 seconds the sun 2
    #y4_site = ["https://www.youtube.com/embed/6tmbeLTHC_0?start=559&end=679;mute=1;autoplay=1", 120] #120 seconds the sun 3
    #y5_site = ["https://www.youtube.com/embed/6tmbeLTHC_0?start=1059&end=1359;mute=1;autoplay=1", 300] #300 seconds the sun 4
    #y6_site = ["https://www.youtube.com/embed/7fYKMCCPh28?start=53&end=118;mute=1;autoplay=1", 65] #65 seconds earth 1
    #y7_site = ["https://www.youtube.com/embed/7fYKMCCPh28?start=988&end=1043;mute=1;autoplay=1", 55] #55 seconds earth 2
    #y8_site = ["https://www.youtube.com/embed/7fYKMCCPh28?start=1196&end=1826;mute=1;autoplay=1", 630] #630 seconds earth 3
    #y9_site = ["https://www.youtube.com/embed/7fYKMCCPh28?start=1828&end=2175;mute=1;autoplay=1", 347] #347 seconds earth 4
    #y10_site = ["https://www.youtube.com/embed/PBJAR3-UvSQ?start=29&end=289;mute=1;autoplay=1", 260] #260 seconds aurora
    #y11_site = ["https://www.youtube.com/embed/Ilifg26TZrI?mute=1;autoplay=1", 144] #144 seconds around the moon
    #videos = [y1_site, y2_site, y3_site, y4_site, y5_site, y6_site, y7_site, y8_site, y9_site, y10_site, y11_site]
    

    #site = "http://wttr.in/Saint+Louis+Missouri"
    #site = "https://www.msn.com/en-us/news/"
    #site43 = "https://www.mlb.com/postseason"
    #site = "http://wttr.in/Saint+Louis+Missouri"
    #site = "https://spotthestation.nasa.gov/sightings/view.cfm?country=United_States&region=Missouri&city=Jefferson_National_Expansion_Memorial"
    #site = "https://www.youtube.com/watch?v=DDU-rZs-Ic4"
    #site = "https://www.youtube.com/watch?v=EEIk7gwjgIM"
    #site = "https://spotthestation.nasa.gov/tracking_map.cfm"
    #site = "http://www.internettrafficreport.com/"
    #site = "https://cybermap.kaspersky.com"
    #site = "https://www.akamai.com/us/en/resources/visualizing-akamai/enterprise-threat-monitor.jsp"
    #site = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
    #site = "https://console.rumble.run"
    #site = "https://www.youtube.com/embed/eJ7ZkQ5TC08?mute=1;autoplay=1"
    #site ="https://map.internetintel.oracle.com/?root=national&country=US"
    #site = "https://www.youtube.com/embed/GAv4VCC41oU?mute=1;autoplay=1"
    #site62 = ["https://www.nasa.gov/specials/trackartemis/", 180] # Artemis tracker
