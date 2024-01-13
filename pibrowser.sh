#!/bin/bash
#sleep 60
# Add this to~/.config/lxsession/LXDE-pi/autostart:
#@lxterminal -e ~/pibrowser.sh
#hide the mouse cursor
#@unclutter -idle 0


a=1

while [ $a -le 2 ]
do

  firefox-esr --kiosk 'http://magicmirror.findley.cc:8080' &
  sleep 240
  kill %1

  firefox-esr --kiosk 'https://www.pollen.com/forecast/current/pollen/63132' &
  sleep 30
  kill %1

  firefox-esr --kiosk 'http://en.blitzortung.org/live_lightning_maps.php?map=30' &
  sleep 30
  kill %1

  firefox-esr --kiosk 'https://www.wunderground.com/wundermap?lat=37.7&lon=-92.7&zoom=4&radar=1&wxstn=0' &
  sleep 12
  kill %1

  firefox-esr --kiosk 'http://magicmirror.findley.cc:8080' &
  sleep 180
  kill %1

 # firefox-esr --kiosk 'https://radar.weather.gov/?settings=v1_eyJhZ2VuZGEiOnsiaWQiOiJ3ZWF0aGVyIiwiY2VudGV' &
 # sleep 60
 # kill %1

  firefox-esr --kiosk 'https://www.wunderground.com/wundermap' &
  sleep 60
  kill %1

  firefox-esr --kiosk 'https://www.wunderground.com/dashboard/pws/KMOSTLOU477' &
  sleep 60
  kill %1

done