#Created October 2020 ptf
#basis: https://www.geeksforgeeks.org/build-an-application-to-extract-news-from-google-news-feed-using-python/

from gnewsclient import gnewsclient        
import time                                
import requests                             
from datetime import datetime, timedelta    
import feedparser
import sys

#Validate we are online, since everything is internet-based.  Quit if not.
try:
    if requests.get('http://1.1.1.1').ok:
        print("You're Online")
except:
    print("You're Offline")
    sys.quit()

TTOPICS = ['technology', 'business', 'world', 'nation', 'sport']
CWHITE =  '\33[37m'
CCYAN = '\33[36m'
CGREEN = '\33[32m'
CEND = '\33[0m'
CWHITE2 = '\33[97m'
CBLUE2 = '\33[94m'
CGREY    = '\33[90m'
CYELLOW2 = '\33[93m'

VAR_RSS = ['https://www.aljazeera.com/xml/rss/all.xml',
               'https://hnrss.org/frontpage',       
               'https://www.zdnet.com/news/rss.xml']
TOTAL_RSS = 3
TOTAL_ENTRIES = TOTAL_RSS * 4
NOW = datetime.now()
LATER = datetime.now() + timedelta(minutes=31)
RSS_RESET = 0
FEED_ARRAY = []


TICKER=1
while (TICKER != 0):    #because why not?  runs until killed

#Read Google news feeds and display
    for TTOPIC in TTOPICS:
        client = gnewsclient.NewsClient(language='english',
                            location='United States',
                            topic=TTOPIC,
                            max_results=3)

        news_list = client.get_news()
        for item in news_list:
            print(CWHITE2 + "Title : ", item['title'] + CEND)
            print(CGREY + "Link : " + CBLUE2, item['link'] + CEND)
            print("")
            time.sleep(4)

#generates txt weather report.  Uses OS-defined location
    VAR_URL="http://wttr.in/stl?2n"
    VAR_RES = requests.get(VAR_URL)
    print(VAR_RES.text)
    time.sleep(5)

#Start of the RSS Feed
#We only want to poll RSS Feeds twice per hour
    if RSS_RESET == 0:                                     
        RSS_CNTR = 0                                               
        ARRAY_CNT = 0                                      
        ENTRY_LOOP = 0
        print(CGREEN + "Refreshing RSS feeds" + CEND)
                                          
        while RSS_CNTR < TOTAL_RSS:
            RSSENTRY = feedparser.parse(VAR_RSS[RSS_CNTR])
            E_CNT = len(RSSENTRY['entries'])
            if E_CNT > 4:
                E_CNT = 4                    
            while ENTRY_LOOP < E_CNT:                     
                FEEDENTRY = RSSENTRY.entries[ENTRY_LOOP]
                if FEEDENTRY == None:
                    pass
                else:
                    FEED_ARRAY.append(FEEDENTRY)
                    ARRAY_CNT += 1
                ENTRY_LOOP += 1                                                                                                             
            ENTRY_LOOP = 0
            RSS_CNTR += 1                                  
        RSS_RESET = 1                                       
    else:
        print(CGREEN + "Recycling RSS feeds" + CEND)    
    ENTRY_NO = 0

    while ENTRY_NO < ARRAY_CNT:
        entry = FEED_ARRAY[ENTRY_NO]
        print(CWHITE2 + entry.published + CEND)
        print(CYELLOW2 + "******" + CEND)
        print(CGREY + entry.summary + CEND)
        print(CBLUE2 + "------News Link--------")
        print(CBLUE2 + entry.link + CEND)
        time.sleep(5)
        ENTRY_NO += 1

    if NOW >= LATER: 
        LATER = datetime.now() + timedelta(minutes=31)
        RSS_RESET = 0
    print (CGREEN + "End of Cycle" + CEND)


#Black: \u001b[30m.
#Red: \u001b[31m.
# #Green: \u001b[32m.
#Yellow: \u001b[33m.
#Blue: \u001b[34m.
#Magenta: \u001b[35m.
#Cyan: \u001b[36m.
#White: \u001b[37m.


