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

site01 = ["https://npr.org", 180]
site02 = ["https://www.kmov.com/news/", 180]
site03 = ["https://www.pollen.com/forecast/current/pollen/63132", 120]
#site04 = NOAA STL forecast
site04 = ["https://forecast.weather.gov/MapClick.php?CityName=Olivette&state=MO&site=LSX&textField1=38.6723&textField2=-90.3772&e=0", 180]
#site05 = Wunderground US Radar
site05 = ["https://www.wunderground.com/wundermap?lat=37.7&lon=-92.7&zoom=4&radar=1&wxstn=0", 180]
site06 = ["http://en.blitzortung.org/live_lightning_maps.php?map=30", 180]
site07 = ["https://ncov2019.live/", 60]
site08 = ["https://ncov2019.live/data/unitedstates", 60]
site10 = ["https://www.flightradar24.com/40.52,-101.43/4", 240]
#site11 = NOAA STL Radar
site11 = ["https://radar.weather.gov/?settings=v1_eyJhZ2VuZGEiOnsiaWQiOiJ3ZWF0aGVyIiwiY2VudGVyIjpbLTkwLjIsMzguNjI4XSwiem9vbSI6NywibG9jYXRpb24iOlstOTAuMiwzOC42MjhdfSwiYmFzZSI6InN0YW5kYXJkIiwiY291bnR5IjpmYWxzZSwiY3dhIjpmYWxzZSwic3RhdGUiOmZhbHNlLCJtZW51Ijp0cnVlLCJzaG9ydEZ1c2VkT25seSI6ZmFsc2V9#/", 120]
#site12 = wunderground temp readings
site12 = ["https://www.wunderground.com/wundermap", 120]
site13 = ["https://www.wunderground.com/dashboard/pws/KMOSTLOU477", 180]
site14 = ["https://www.bbc.com/", 180]
site15 = ["https://www.newsbreak.com/missouri/st.-louis", 180]
site16 = ["https://www.bizjournals.com/stlouis/news/", 180]
site17 = ["https://www.stltoday.com/news/#tracking-source=main-nav", 180]
site18 = ["https://www.stltoday.com/sports/", 180]
site19 = ["https://feedreader.com/online/#/reader/category/all/", 240]
site20 = ["https://www.mlb.com/cardinals", 180]
site21 = ["https://www.nhc.noaa.gov", 120]
site22 = ["https://www.youtube.com/embed/eJ7ZkQ5TC08?mute=1;autoplay=1", 180] #Times Square
site23 = ["https://mars.nasa.gov/mars2020/mission/where-is-the-rover/", 120]
site24 = ["https://www.earthcam.com/usa/missouri/stlouis/?cam=arch_riverview", 180]
site25 = ["https://www.earthcam.com/usa/florida/keywest/?cam=irishkevins", 180]
site26 = ["https://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1", 180]
site27 = ["https://www.earthcam.com/usa/florida/miami/resort/?cam=miamiresort", 180]
site28 = ["https://www.earthcam.com/world/czechrepublic/prague/?cam=grandhotel_str", 180]
site29 = ["https://www.earthcam.com/world/netherlands/amsterdam/?cam=amsterdam", 180]
site30 = ["https://www.earthcam.com/world/aruba/druifbeach/?cam=casadelmar2", 180]
site31 = ["https://www.earthcam.com/usa/nevada/lasvegas/fremontstreet/?cam=catsmeow_lv_fremont", 240]
site32 = ["https://www.earthcam.com/usa/illinois/chicago/field/?cam=fieldmuseum", 180]
site33 = ["https://www.earthcam.com/world/ireland/dublin/?cam=templebar", 180]
site34 = ["https://www.earthcam.com/world/canada/niagarafalls/?cam=niagarafalls_str", 180]
site36 = ["https://www.purpleair.com/map?opt=1/mAQI/a10/cC0#3.49/39.72/-98.65", 180]
site35 = ["https://coinmarketcap.com/watchlist", 180]
site37 = ["https://www.earthcam.com/usa/louisiana/neworleans/bourbonstreet/?cam=catsmeow2", 180]
# site38 = MSN STL forecast
site38 = ["https://www.msn.com/en-us/weather/today/weather-today/we-city?el=mqNeq4S2Ru16490udqmjjQ2VhRd7uNY42E%2BdrD3Q1rCRPcvzkGBdbSYZZ%2FwLZjzYmVTDoKVUfspPezxGz6SXCTkAjRSdk4A7DAmW2MAOT2sGnBCTLuacmCaSfmfCUWZwsU%2BX8djG%2FubYIauiqUQ13Q%3D%3D&weadegreetype=F&ocid=winp1taskbar", 180]
# site 39 = MSN STL Radar
site39 = ["https://www.msn.com/en-us/weather/maps/weather-today/we-city?weadegreetype=F&ocid=winp1taskbar&lat=38.66826248&lon=-90.45602417&weaext0=%7B%22l%22%3A%22St+Louis%22%2C%22r%22%3A%22MO%22%2C%22c%22%3A%22United+States%22%2C%22i%22%3A%22US%22%2C%22g%22%3A%22en-us%22%7D&city=St+Louis%2C+MO&type=radar&animation=1", 180]
# site 40 = MSN STL temp
site40 = ["https://www.msn.com/en-us/weather/maps/weather-today/we-city?weadegreetype=F&ocid=winp1taskbar&lat=38.66826248&lon=-90.45602417&weaext0=%7B%22l%22%3A%22St+Louis%22%2C%22r%22%3A%22MO%22%2C%22c%22%3A%22United+States%22%2C%22i%22%3A%22US%22%2C%22g%22%3A%22en-us%22%7D&city=St+Louis%2C+MO&type=temperature&animation=1",120]
# site41 = MSN hurricane
site41 = ["https://www.msn.com/en-us/weather/maps/weather-today/we-city?weadegreetype=F&ocid=winp1taskbar&lat=38.66826248&lon=-90.45602417&weaext0=%7B%22l%22%3A%22St+Louis%22%2C%22r%22%3A%22MO%22%2C%22c%22%3A%22United+States%22%2C%22i%22%3A%22US%22%2C%22g%22%3A%22en-us%22%7D&city=St+Louis%2C+MO&type=hurricane&animation=1&zoom=4",180]
site42 = ["https://www.msn.com/en-us/feed",180]
site43 = ["https://www.mlb.com/postseason",180]


websites = [site01, site02, site03, site38, site05, \
    site06, site10, \
        site11, site39, site12, site40, site13, site14, \
          site16, site17, site18, \
              site21, site41, site23, site24, site25, \
                  site26, site29, site31, site33, site35, site36, site37, \
                      site42 ]



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
