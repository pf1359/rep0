# My first Python script!  I found something to do with it.
# Pat Findley 5 May 2020, in the midst of COVID-19 lockdown
# To get Firefox to open pages in the same tab, you have to make these changes in about:config:
# browser.link.open_newwindow.restriction = 0
# browser.link.open_newwindow = 1
# modified 11 May to cleanup the loop. ptf

import webbrowser
import time

x = 0
y = 0
while x < 100:

   a_website = "https://cnn.com"
   b_website = "https://npr.org"
  #b _website = "https://stltoday.com"
   d_website = "https://www.pollen.com/forecast/current/pollen/63132"
   e_website = "https://forecast.weather.gov/MapClick.php?CityName=Olivette&state=MO&site=LSX&textField1=38.6723&textField2=-90.3772&e=0"
   c_website = "http://en.blitzortung.org/live_lightning_maps.php?map=30"
   f_website = "http://wunderground.com/radar/us"
   g_website = "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

   while y < 10:
      webbrowser.get('Firefox').open(a_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(b_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(c_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(d_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(e_website, new=0)
      time.sleep(300)

      webbrowser.get('Firefox').open(f_website, new=0)
      time.sleep(300)
   y+=1

   webbrowser.get('Firefox').open(g_website, new=0)
   time.sleep(300)
x+=1
