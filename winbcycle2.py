# My first Python script!  I found something to do with it.
# Pat Findley 5 May 2020, in the midst of COVID-19 lockdown
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# Remember to go into options and enable autoplay audio and video if using Youtube links
    #from selenium import webdriver
    #driver = webdriver.Chrome()
    #driver.get(link1)

import webbrowser
import time
#import random
firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe %s"
#webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))

VAR_CYCLE = 1
while VAR_CYCLE > 0:

     #b = NPR home page
    b_website = "https://npr.org"
    webbrowser.open(b_website, new=0)
    time.sleep(180)

    #h = KMOV news page
    h_website = "https://www.kmov.com/news/"
    webbrowser.open(h_website, new=0)
    time.sleep(180)

    #d = Pollen count for STL
    d_website = "https://www.pollen.com/forecast/current/pollen/63132"
    webbrowser.open(d_website, new=0)
    time.sleep(60)

    #e = NOAA weather forcast for STL
    e_website = "https://forecast.weather.gov/MapClick.php?CityName=Olivette&state=MO&site=LSX&textField1=38.6723&textField2=-90.3772&e=0"
    webbrowser.open(e_website, new=0)
    time.sleep(180)

    #f = US weather radar
    f_website = "https://www.wunderground.com/wundermap?lat=37.7&lon=-92.7&zoom=4&radar=1&wxstn=0"
    webbrowser.open(f_website, new=0)
    time.sleep(240)

    #c = Blitzortung US lightning map
    c_website = "http://en.blitzortung.org/live_lightning_maps.php?map=30"
    webbrowser.open(c_website, new=0)
    time.sleep(120)

    #i = COVID-19 live stats page
    i_website = "https://ncov2019.live/"
    webbrowser.open(i_website, new=0)
    time.sleep(120)

    #ia = COVID-19 US live stats page (added 22Aug2020)
    ia_website = "https://ncov2019.live/data/unitedstates"
    webbrowser.open(ia_website, new=0)
    time.sleep(120)

    #o = Meraki site for Findley
    #o_website = "https://n340.meraki.com/o/oci4od/manage/new_reports"
    o_website = "https://n340.meraki.com/1000Llewellyn-wi/n/fGBARc0c/manage/usage/list?timespanClient=7200"
    webbrowser.open(o_website, new=0)
    time.sleep(120)

    #p = FlightRadar 24.  use with findleytablet@gmail.com for best result
    p_website = "https://www.flightradar24.com/40.52,-101.43/4"
    webbrowser.open(p_website, new=0)
    time.sleep(300)
   
    #s = radar loop
    s_website = "https://radar.weather.gov/?settings=v1_eyJhZ2VuZGEiOnsiaWQiOiJ3ZWF0aGVyIiwiY2VudGVyIjpbLTkwLjIsMzguNjI4XSwiem9vbSI6NywibG9jYXRpb24iOlstOTAuMiwzOC42MjhdfSwiYmFzZSI6InN0YW5kYXJkIiwiY291bnR5IjpmYWxzZSwiY3dhIjpmYWxzZSwic3RhdGUiOmZhbHNlLCJtZW51Ijp0cnVlLCJzaG9ydEZ1c2VkT25seSI6ZmFsc2V9#/"
    webbrowser.open(s_website, new=0)
    time.sleep(180)

    #ab = wundermap local stations (add 30 Aug 2020)
    ab_website = "https://www.wunderground.com/wundermap"
    webbrowser.open(ab_website, new=0)
    time.sleep(180)

    #ap = a Creve Coeur weather underground station
    #olivette = https://www.wunderground.com/dashboard/pws/KMOOLIVE2
    #stoneleigh = https://www.wunderground.com/dashboard/pws/KMOSTLOU343
    ap_website = "https://www.wunderground.com/dashboard/pws/KMOSTLOU477"
    webbrowser.open(ap_website, new=0)
    time.sleep(180)
    
    #y = BBC news (add 22 Aug 2020)
    y_website = "https://www.bbc.com/"
    webbrowser.open(y_website, new=0)
    time.sleep(180)

    #z = Newsbreak St. Louis (add 22 Aug 2020)
    z_website = "https://www.newsbreak.com/missouri/st.-louis"
    webbrowser.open(z_website, new=0)
    time.sleep(180)

    #am = stl business journal (requires sign-in, added 10Jan21)
    am_website = "https://www.bizjournals.com/stlouis/news/"
    webbrowser.open(am_website, new=0)
    time.sleep(120)

    ah_website = "https://www.stltoday.com/news/#tracking-source=main-nav"
    firefox.open(ah_website, new=0)
    time.sleep(120)

    ai_website = "https://www.stltoday.com/sports/"
    webbrowser.open(ai_website, new=0)
    time.sleep(120)

    #an - feedreader (added 19Feb21.  Sign in as findleytablet) 
    an_website = "https://feedreader.com/online/#/reader/category/all/"
    webbrowser.open(an_website, new=0)
    time.sleep(180)
  
    #w = Cardinals
    w_website = "https://www.mlb.com/cardinals"
    webbrowser.open(w_website, new=0)
    time.sleep(180)

    #t = hurricane watch
    t_website = "https://www.nhc.noaa.gov"
    webbrowser.open(t_website, new=0)
    time.sleep(180)

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
    
    # do we feel lucky?
    #modified to remove the link since Firefox broke autoplay
    #if chance >= 11:
    #    selection = random.choice(videos)
    #    firefox.open(selection[0], new=0)
    #    time.sleep(selection[1])
    #else:
        #r = text weather in STL
        #r_website = "http://wttr.in/Saint+Louis+Missouri"
        #firefox.open(r_website, new=0)
        #time.sleep(60)

        #latest = Ap - 10Apr21

    #a = MSN news page
    #a_website = "https://www.msn.com/en-us/news/"
    #firefox.open(a_website, new=0)
    #time.sleep(180)
    #ae_website = "https://www.mlb.com/postseason"
    #firefox.open(ae_website, new=0)
    #time.sleep(180)



    #r = text weather in STL
    #r_website = "http://wttr.in/Saint+Louis+Missouri"
    #u = ISS watch
    #u_website = "https://spotthestation.nasa.gov/sightings/view.cfm?country=United_States&region=Missouri&city=Jefferson_National_Expansion_Memorial"
    #v = Deerfield Beach Underwater Camera

    #x = Live feed from ISS (added 13Aug2020, removed 14Aug2020)
    #x_website = "https://www.youtube.com/watch?v=DDU-rZs-Ic4"

    #j = Live feed from ISS
    #j_website = "https://www.youtube.com/watch?v=EEIk7gwjgIM"
    #firefox.open(j_website, new=0)
    #time.sleep(300)
    #k = ISS location
    #k_website = "https://spotthestation.nasa.gov/tracking_map.cfm"
    #l = internet traffic report
    #l_website = "http://www.internettrafficreport.com/"
    #m = Kaspersky attack visualization
    #m_website = "https://cybermap.kaspersky.com"
    #n = Akamai threat monitor
    #n_website = "https://www.akamai.com/us/en/resources/visualizing-akamai/enterprise-threat-monitor.jsp"

    #g = COVID-19 research map
    #g_website = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
    #firefox.open(g_website, new=0)
    #time.sleep(60)

    #ag = rumble console (run as reed honely, added 18Oct2020)
    #ag_website = "https://console.rumble.run"
    #firefox.open(ag_website, new=0)
    #time.sleep(120)

    #Disabled 14Feb21 because Firefox broke autoplay
    #al = youtube live feed NYC Times Square
    #al_website = "https://www.youtube.com/embed/eJ7ZkQ5TC08?mute=1;autoplay=1"
    #firefox.open(al_website, new=0)
    #time.sleep(120)

        #aa = Oracle Internet Intelligence internet uptime (add 30 Aug 2020)
    #aa_website="https://map.internetintel.oracle.com/?root=national&country=US"
    #firefox.open(aa_website, new=0)
    #time.sleep(120)
    
    #youtube live feed deerfield beach
    #v_website = "https://www.youtube.com/embed/GAv4VCC41oU?mute=1;autoplay=1"
    #firefox.open(v_website, new=0)
    #time.sleep(180)

    #ad = pihole on rpi419a(mod 4 Dec 2020)
    #ad_website = "http://dns4.findley.cc/admin/"
    #firefox.open(ad_website, new=0)
    #time.sleep(120)

    #af = pihole on rpi0wrw (add 14 Oct 2020)
    #af_website = "http://dns3.findley.cc/admin/"
    #firefox.open(af_website, new=0)
    #time.sleep(120)

    #ao = pihole docker on 780white (add 15 Feb 2021)
    #ao_website = "http://dns5.findley.cc/admin/"
    #firefox.open(ao_website, new=0)
    #time.sleep(120)