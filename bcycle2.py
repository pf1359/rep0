# My first Python script!  I found something to do with it.
# Pat Findley 5 May 2020, in the midst of COVID-19 lockdown
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# Remember to go into options and enable autoplay audio and video if using Youtube links

import webbrowser
import time

VAR_CYCLE = 1
while VAR_CYCLE > 0:

   

    #b = NPR home page
    b_website = "https://npr.org"
    webbrowser.get('Firefox').open(b_website, new=0)
    time.sleep(180)

    #h = KMOV news page
    h_website = "https://www.kmov.com/news/"
    webbrowser.get('Firefox').open(h_website, new=0)
    time.sleep(180)

    #d = Pollen count for STL
    d_website = "https://www.pollen.com/forecast/current/pollen/63132"
    webbrowser.get('Firefox').open(d_website, new=0)
    time.sleep(120)

    #e = NOAA weather forcast for STL
    e_website = "https://forecast.weather.gov/MapClick.php?CityName=Olivette&state=MO&site=LSX&textField1=38.6723&textField2=-90.3772&e=0"
    webbrowser.get('Firefox').open(e_website, new=0)
    time.sleep(180)

    #f = US weather radar
    f_website = "http://wunderground.com/radar/us"
    webbrowser.get('Firefox').open(f_website, new=0)
    time.sleep(240)

    #c = Blitzortung US lightning map
    c_website = "http://en.blitzortung.org/live_lightning_maps.php?map=30"
    webbrowser.get('Firefox').open(c_website, new=0)
    time.sleep(120)

    #i = COVID-19 live stats page
    i_website = "https://ncov2019.live/"
    webbrowser.get('Firefox').open(i_website, new=0)
    time.sleep(120)

    #ia = COVID-19 US live stats page (added 22Aug2020)
    ia_website = "https://ncov2019.live/data/unitedstates"
    webbrowser.get('Firefox').open(ia_website, new=0)
    time.sleep(120)

    #o = Meraki site for Findley
    o_website = "https://n340.meraki.com/1000Llewellyn-wi/n/fGBARc0c/manage/usage/list?timespanClient=7200"
    webbrowser.get('Firefox').open(o_website, new=0)
    time.sleep(120)

    #p = FlightRadar 24.  use with findleytablet@gmail.com for best result
    p_website = "https://www.flightradar24.com/40.52,-101.43/4"
    webbrowser.get('Firefox').open(p_website, new=0)
    time.sleep(300)
   
    #s = radar loop
    s_website = "https://radar.weather.gov/?settings=v1_eyJhZ2VuZGEiOnsiaWQiOiJ3ZWF0aGVyIiwiY2VudGVyIjpbLTkwLjIsMzguNjI4XSwiem9vbSI6NywibG9jYXRpb24iOlstOTAuMiwzOC42MjhdfSwiYmFzZSI6InN0YW5kYXJkIiwiY291bnR5IjpmYWxzZSwiY3dhIjpmYWxzZSwic3RhdGUiOmZhbHNlLCJtZW51Ijp0cnVlLCJzaG9ydEZ1c2VkT25seSI6ZmFsc2V9#/"
    webbrowser.get('Firefox').open(s_website, new=0)
    time.sleep(180)

    #ab = wundermap local stations (add 30 Aug 2020)
    ab_website = "https://www.wunderground.com/wundermap"
    webbrowser.get('Firefox').open(ab_website, new=0)
    time.sleep(180)
    
    #y = BBC news (add 22 Aug 2020)
    y_website = "https://www.bbc.com/"
    webbrowser.get('Firefox').open(y_website, new=0)
    time.sleep(180)

    #z = Newsbreak St. Louis (add 22 Aug 2020)
    z_website = "https://www.newsbreak.com/missouri/st.-louis"
    webbrowser.get('Firefox').open(z_website, new=0)
    time.sleep(180)

    #aa = Oracle Internet Intelligence internet uptime (add 30 Aug 2020)
    aa_website="https://map.internetintel.oracle.com/?root=national&country=US"
    webbrowser.get('Firefox').open(aa_website, new=0)
    time.sleep(120)

    v_website = "https://www.youtube.com/embed/GAv4VCC41oU?mute=1;autoplay=1"
    webbrowser.get('Firefox').open(u_website, new=0)
    time.sleep(180)

    #ad = pihole on rpi419a(mod 4 Dec 2020)
    ad_website = "http://dns.findley.cc/admin/"
    webbrowser.get('Firefox').open(ad_website, new=0)
    time.sleep(120)

    #af = pihole on rpi0wrw (add 14 Oct 2020)
    af_website = "http://dns3.findley.cc/admin/"
    webbrowser.get('Firefox').open(af_website, new=0)
    time.sleep(120)

    #ag = rumble console (run as reed honely, added 18Oct2020)
    ag_website = "https://console.rumble.run"
    webbrowser.get('Firefox').open(ag_website, new=0)
    time.sleep(120)

    #al = youtube live feed NYC Times Square
    al_website = "https://www.youtube.com/embed/eJ7ZkQ5TC08?mute=1;autoplay=1"
    webbrowser.get('Firefox').open(al_website, new=0)
    time.sleep(120)

    ah_website = "https://www.stltoday.com/news/#tracking-source=main-nav"
    webbrowser.get('Firefox').open(ah_website, new=0)
    time.sleep(120)

    ai_website = "https://www.stltoday.com/sports/"
    webbrowser.get('Firefox').open(ai_website, new=0)
    time.sleep(120)

    #latest = AL 26Dec2020

    #a = MSN news page
    #a_website = "https://www.msn.com/en-us/news/"
    #webbrowser.get('Firefox').open(a_website, new=0)
    #time.sleep(180)
    #ae = MLB Postseason (maybe next year....)
    #ae_website = "https://www.mlb.com/postseason"
    #webbrowser.get('Firefox').open(ae_website, new=0)
    #time.sleep(180)
    #t = hurricane watch
    #t_website = "https://www.nhc.noaa.gov"
    #webbrowser.get('Firefox').open(t_website, new=0)
    #time.sleep(180)

   
    #w = Cardinals (removed when their 2020 season ended)
    #w_website = "https://www.mlb.com/cardinals"
    #webbrowser.get('Firefox').open(w_website, new=0)
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
    #webbrowser.get('Firefox').open(j_website, new=0)
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
    #webbrowser.get('Firefox').open(g_website, new=0)
    #time.sleep(60)