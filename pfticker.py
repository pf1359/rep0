#Created October 2020 ptf
#basis: https://www.geeksforgeeks.org/build-an-application-to-extract-news-from-google-news-feed-using-python/

import gnewsclient
from gnewsclient import gnewsclient # for the google newsfeed
import time # for sleep
import requests #for the wttr.in request

TTOPICS = ['technology', 'business', 'world', 'nation', 'sport']
CWHITE =  '\33[37m'
CCYAN = '\33[36m'
CGREEN = '\33[32m'
CEND = '\33[0m'
CWHITE2 = '\33[97m'
CBLUE2 = '\33[94m'
CGREY    = '\33[90m'

#need to slow this down
#feeds don't like to be polled more than twice per hour
ticker=1
while (ticker != 0):    #because why not?  runs until killed
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

        time.sleep(6)

    #generates txt weather report.  Uses OS-defined location
    VAR_URL="http://wttr.in/stl?2n"
    VAR_RES = requests.get(VAR_URL)
    print(VAR_RES.text)
    time.sleep(30)

    


    print (CGREEN + "End of Cycle" + CEND)


#Black: \u001b[30m.
#Red: \u001b[31m.
# #Green: \u001b[32m.
#Yellow: \u001b[33m.
#Blue: \u001b[34m.
#Magenta: \u001b[35m.
#Cyan: \u001b[36m.
#White: \u001b[37m.

#https://www.aljazeera.com/xml/rss/all.xml
#https://feeds.npr.org/500005/podcast.xml
#https://kwmu-rss.streamguys1.com/gateway/gateway.xml
#http://rss.slashdot.org/Slashdot/slashdotMain
#https://hnrss.org/frontpage
#https://www.zdnet.com/news/rss.xml

