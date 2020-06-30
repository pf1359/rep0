# My first Python script!  I found something to do with it.
# Pat Findley 5 May 2020, in the midst of COVID-19 lockdown
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# modified 11 May to cleanup the loop. ptf
# modified 25 May to add more content and comments. ptf

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
   #c = Blitzortung US lightning mape
   c_website = "http://en.blitzortung.org/live_lightning_maps.php?map=30"
   #f = US weather radar
   f_website = "http://wunderground.com/radar/us"
   #g = COVID-19 research map
   g_website = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"
   #h = KMOV news page
   h_website = "https://www.kmov.com/news/"
   #i = COVID-19 live stats pageag
   i_website = "https://ncov2019.live/"
   #j = Live feed from ISS
   #j_website = "https://www.youtube.com/watch?v=EEIk7gwjgIM"
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

   while y < 10:
      webbrowser.get('Firefox').open(a_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(f_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(c_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(d_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(n_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(e_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(b_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(h_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(i_website, new=0)
      time.sleep(300)

      #webbrowser.get('Firefox').open(j_website, new=0)
      #time.sleep(300)

      webbrowser.get('Firefox').open(p_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(o_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(g_website, new=0)
      time.sleep(300)
   y+=1
x+=1
