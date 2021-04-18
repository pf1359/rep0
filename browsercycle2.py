# Modified version of my script for cross-platform use.
# Pat Findley 17 Apr 2021
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# Remember to go into options and enable autoplay audio and video if using Youtube links
    #from selenium import webdriver
    #driver = webdriver.Chrome()
    #driver.get(link1)
#import random
#firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe %s"
#webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

#IF Linux, we need this and change webbrowser.open to firefox.open
#firefox = webbrowser.get('Firefox')



import webbrowser
import time

site01 = ["https://npr.org", 120]
site02 = ["https://www.kmov.com/news/", 120]
site03 = ["https://www.pollen.com/forecast/current/pollen/63132", 60]
site04 = ["https://forecast.weather.gov/MapClick.php?CityName=Olivette&state=MO&site=LSX&textField1=38.6723&textField2=-90.3772&e=0", 60]
site05 = ["https://www.wunderground.com/wundermap?lat=37.7&lon=-92.7&zoom=4&radar=1&wxstn=0", 120]
site06 = ["http://en.blitzortung.org/live_lightning_maps.php?map=30", 120]
site07 = ["https://ncov2019.live/", 60]
site08 = ["https://ncov2019.live/data/unitedstates", 60]
site09 = ["]https://n340.meraki.com/1000Llewellyn-wi/n/fGBARc0c/manage/usage/list?timespanClient=7200", 120]
site10 = ["https://www.flightradar24.com/40.52,-101.43/4", 180]
site11 = ["https://radar.weather.gov/?settings=v1_eyJhZ2VuZGEiOnsiaWQiOiJ3ZWF0aGVyIiwiY2VudGVyIjpbLTkwLjIsMzguNjI4XSwiem9vbSI6NywibG9jYXRpb24iOlstOTAuMiwzOC42MjhdfSwiYmFzZSI6InN0YW5kYXJkIiwiY291bnR5IjpmYWxzZSwiY3dhIjpmYWxzZSwic3RhdGUiOmZhbHNlLCJtZW51Ijp0cnVlLCJzaG9ydEZ1c2VkT25seSI6ZmFsc2V9#/", 180]
site12 = ["https://www.wunderground.com/wundermap", 180]
site13 = ["https://www.wunderground.com/dashboard/pws/KMOSTLOU477", 180]
site14 = ["https://www.bbc.com/", 120]
site15 = ["https://www.newsbreak.com/missouri/st.-louis", 120]
site16 = ["https://www.bizjournals.com/stlouis/news/", 120]
site17 = ["https://www.stltoday.com/news/#tracking-source=main-nav", 120]
site18 = ["https://www.stltoday.com/sports/", 120]
site19 = ["https://feedreader.com/online/#/reader/category/all/", 240]
site20 = ["https://www.mlb.com/cardinals", 120]
site21 = ["https://www.nhc.noaa.gov", 120]
site22 = ["https://www.youtube.com/embed/eJ7ZkQ5TC08?mute=1;autoplay=1", 180]

websites = [site01, site02, site03, site04, site05, site06, site07, site08, site09, \
     site10, site11, site12, site13, site14, site15, site16, site17, site18, site19, \
         site20, site21, site22]


VAR_CYCLE = 1
while VAR_CYCLE > 0:
   for website in websites:
      webbrowser.open(website[0], new=0)
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
    

    #r_website = "http://wttr.in/Saint+Louis+Missouri"
    #a_website = "https://www.msn.com/en-us/news/"
    #ae_website = "https://www.mlb.com/postseason"
    #r_website = "http://wttr.in/Saint+Louis+Missouri"
    #u_website = "https://spotthestation.nasa.gov/sightings/view.cfm?country=United_States&region=Missouri&city=Jefferson_National_Expansion_Memorial"
    #x_website = "https://www.youtube.com/watch?v=DDU-rZs-Ic4"
    #j_website = "https://www.youtube.com/watch?v=EEIk7gwjgIM"
    #k_website = "https://spotthestation.nasa.gov/tracking_map.cfm"
    #l_website = "http://www.internettrafficreport.com/"
    #m_website = "https://cybermap.kaspersky.com"
    #n_website = "https://www.akamai.com/us/en/resources/visualizing-akamai/enterprise-threat-monitor.jsp"
    #g_website = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
    #ag_website = "https://console.rumble.run"
    #al_website = "https://www.youtube.com/embed/eJ7ZkQ5TC08?mute=1;autoplay=1"
    #aa_website="https://map.internetintel.oracle.com/?root=national&country=US"
    #v_website = "https://www.youtube.com/embed/GAv4VCC41oU?mute=1;autoplay=1"
    #ad_website = "http://dns4.findley.cc/admin/"
    #af_website = "http://dns3.findley.cc/admin/"
    #ao_website = "http://dns5.findley.cc/admin/"
