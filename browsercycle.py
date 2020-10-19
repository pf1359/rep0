# My first Python script!  I found something to do with it.
# Pat Findley 5 May 2020, in the midst of COVID-19 lockdown
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# Remember to go into options and enable autoplay audio and video if using Youtube links
# 13 Aug 2020 - adjusted timing
# 10 Oct 2020 - reduced timing on most pages


import webbrowser
import time

x = 0
y = 0
while x < 100:

   #a = MSN news page
   a_website = "https://www.msn.com/en-us/news/"
   #b = NPR home page
   b_website = "https://npr.org"
   #d = Pollen count for STL
   d_website = "https://www.pollen.com/forecast/current/pollen/63132"
   #e = NOAA weather forcast for STL
   e_website = "https://forecast.weather.gov/MapClick.php?CityName=Olivette&state=MO&site=LSX&textField1=38.6723&textField2=-90.3772&e=0"
   #c = Blitzortung US lightning map
   c_website = "http://en.blitzortung.org/live_lightning_maps.php?map=30"
   #f = US weather radar
   f_website = "http://wunderground.com/radar/us"
   #g = COVID-19 research map
   g_website = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
   #h = KMOV news page
   h_website = "https://www.kmov.com/news/"
   #i = COVID-19 live stats page
   i_website = "https://ncov2019.live/"
   #ia = COVID-19 US live stats page (added 22Aug2020)
   ia_website = "https://ncov2019.live/data/unitedstates"
   #j = Live feed from ISS
   j_website = "https://www.youtube.com/watch?v=EEIk7gwjgIM"
   #k = ISS location
   k_website = "https://spotthestation.nasa.gov/tracking_map.cfm"
   #l = internet traffic report
   l_website = "http://www.internettrafficreport.com/"
   #m = Kaspersky attack visualization
   m_website = "https://cybermap.kaspersky.com"
   #n = Akamai threat monitor
   n_website = "https://www.akamai.com/us/en/resources/visualizing-akamai/enterprise-threat-monitor.jsp"
   #o = Meraki site for Findley
   o_website = "https://n340.meraki.com/1000Llewellyn-wi/n/fGBARc0c/manage/usage/list?timespanClient=7200"
   #p = FlightRadar 24.  use with findleytablet@gmail.com for best result
   p_website = "https://www.flightradar24.com/40.52,-101.43/4"
   # q = random live feed of a train in Thailand
   q_website = "https://www.youtube.com/watch?v=ywqKR0NKnXQ"
   #r = text weather in STL
   r_website = "http://wttr.in/Saint+Louis+Missouri"
   #s = radar loop
   s_website = "https://radar.weather.gov/ridge/radar_lite.php?rid=LSX&product=NCR&loop=yes"
   #t = hurricane watch
   t_website = "https://www.nhc.noaa.gov"
   #u = ISS watch
   u_website = "https://spotthestation.nasa.gov/sightings/view.cfm?country=United_States&region=Missouri&city=Jefferson_National_Expansion_Memorial"
   #v = Deerfield Beach Underwater Camera
   v_website = "https://www.youtube.com/watch?v=GAv4VCC41oU&feature=youtu.be"
   #w = Cardinals
   w_website = "https://www.mlb.com/cardinals"
   #x = Live feed from ISS (added 13Aug2020, removed 14Aug2020)
   #x_website = "https://www.youtube.com/watch?v=DDU-rZs-Ic4"
   #y = BBC news (add 22 Aug 2020)
   y_website = "https://www.bbc.com/"
   #z = Newsbreak St. Louis (add 22 Aug 2020)
   z_website = "https://www.newsbreak.com/missouri/st.-louis"
   #aa = Oracle Internet Intelligence internet uptime (add 30 Aug 2020)
   aa_website="https://map.internetintel.oracle.com/?root=national&country=US"
   #ab = wundermap local stations (add 30 Aug 2020)
   ab_website = "https://www.wunderground.com/wundermap"
   #ad = pihole on ubuntu820(mod 14 Oct 2020)
   ad_website = "http://dns.findley.cc/admin/"
   #ae = MLB Postseason
   ae_website = "https://www.mlb.com/postseason"
   #af = pihole on rpi0wrw (add 14 Oct 2020)
   af_website = "http://dns2.findley.cc/admin/"
   #ag = rumble console (run as reed honely, added 18Oct2020)
   ag_website = "https://console.rumble.run"

   while y < 10:
      #a = MSN news page (disable 22 Aug 2020)
      #webbrowser.get('Firefox').open(a_website, new=0)
      #time.sleep(300)

      #y = BBC news
      webbrowser.get('Firefox').open(y_website, new=0)
      time.sleep(180)

      #f = US weather radar
      webbrowser.get('Firefox').open(f_website, new=0)
      time.sleep(240)

      #c = Blitzortung US lightning map
      webbrowser.get('Firefox').open(c_website, new=0)
      time.sleep(180)

      #d = Pollen count for STL
      webbrowser.get('Firefox').open(d_website, new=0)
      time.sleep(120)

      #s = radar loop
      webbrowser.get('Firefox').open(s_website, new=0)
      time.sleep(300)

      #ab = wundermap local stations
      webbrowser.get('Firefox').open(ab_website, new=0)
      time.sleep(180)

      #e = NOAA weather forcast for STL
      webbrowser.get('Firefox').open(e_website, new=0)
      time.sleep(180)

      #b = NPR home page
      webbrowser.get('Firefox').open(b_website, new=0)
      time.sleep(240)

      #z = Newsbreak St. Louis
      webbrowser.get('Firefox').open(z_website, new=0)
      time.sleep(180)

      #h = KMOV news page
      webbrowser.get('Firefox').open(h_website, new=0)
      time.sleep(180)

      #i = COVID-19 live stats page
      webbrowser.get('Firefox').open(i_website, new=0)
      time.sleep(120)

      #ia = COVID-19 US live stats page
      webbrowser.get('Firefox').open(ia_website, new=0)
      time.sleep(120)

      #v = Deerfield Beach Underwater Camera (disable 22 Aug 2020)
      #webbrowser.get('Firefox').open(v_website, new=0)
      #time.sleep(300)

      #p = FlightRadar 24.  use with findleytablet@gmail.com for best result
      webbrowser.get('Firefox').open(p_website, new=0)
      time.sleep(300)

      #o = Meraki site for Findley
      webbrowser.get('Firefox').open(o_website, new=0)
      time.sleep(180)

      #g = COVID-19 research map (disabled 22Aug - using too many cpu)
      webbrowser.get('Firefox').open(g_website, new=0)
      time.sleep(90)

      #t = hurricane watch
      webbrowser.get('Firefox').open(t_website, new=0)
      time.sleep(180)

      #u = ISS watch (disable 3 Sep 2020)
      #webbrowser.get('Firefox').open(u_website, new=0)
      #time.sleep(180)

      #w = Cardinals (disable 3 Oct 2020 when they lost)
      #webbrowser.get('Firefox').open(w_website, new=0)
      #time.sleep(180)

      #j = Live feed from ISS (disable 22 Aug 2020)
      #webbrowser.get('Firefox').open(j_website, new=0)
      #time.sleep(300)

      #aa = Oracle Internet Intelligence internet uptime
      webbrowser.get('Firefox').open(aa_website, new=0)
      time.sleep(120)

      #ad = pihole on ubuntu820
      webbrowser.get('Firefox').open(ad_website, new=0)
      time.sleep(120)

      #af = pihole on rpi0wrw
      webbrowser.get('Firefox').open(af_website, new=0)
      time.sleep(120)

      #ae = MLB Postseason (add 27Sep2020)
      webbrowser.get('Firefox').open(ae_website, new=0)
      time.sleep(180)

      #ag = rumble console (added 18 Oct 2020)
      webbrowser.get('Firefox').open(ag_website, new=0)
      time.sleep(120)

   y+=1
x+=1
