#Created October 2020 ptf
#basis: https://www.geeksforgeeks.org/build-an-application-to-extract-news-from-google-news-feed-using-python/

from gnewsclient import gnewsclient        
import time                                                            
from datetime import datetime, timedelta    
import feedparser
import sys


def check_internet():
    #Validate we are online, since everything is internet-based.
    # Quit if not.
    import requests
    try:
        requests.get('http://1.1.1.1', timeout=0.5).ok
        print("You're Online")
    except:
        print("You're offline. Exiting")
        quit()
check_internet()


    
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


    def read_google_news():
        #imports data from Google News Reader and
        #prints top four from each defined topic.
        from gnewsclient import gnewsclient
        import feedparser
        import time
        CEND = '\33[0m'
        CWHITE2 = '\33[97m'
        CBLUE2 = '\33[94m'
        CGREY = '\33[90m'
        categories = ['technology',
                      'business',
                      'world',
                      'nation',
                      'sport']
        for category in categories:
            client = gnewsclient.NewsClient(language='english',
                                            topic=category,
                                            location='United States',
                                            max_results=4)
            news_list = client.get_news()
            for item in news_list:
                print(CWHITE2 + "Title : ", item['title'] + CEND)
                print(CGREY + "Link : " + CBLUE2, item['link'] + CEND)
                print("")
                time.sleep(4)
    read_google_news()

#generates txt weather report.  Uses OS-defined location
    VAR_URL="http://wttr.in/stl?2n"
    import requests
    VAR_RES = requests.get(VAR_URL)
    print(VAR_RES.text)
    time.sleep(10)

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


