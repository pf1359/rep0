#Created October 2020 ptf
#basis: https://www.geeksforgeeks.org/build-an-application-to-extract-news-from-google-news-feed-using-python/
  
import sys
import time
import requests
from datetime import datetime, timedelta
# Set the time for the RSS reader later.
# We don't want to poll RSS more than twice an hour
time_reset = 0
later = datetime.now() + timedelta(minutes=31)
#wonky shit because you can't compare two datetimes without stripping the details
rss_reset_time = later.strftime("%X")

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

def read_google_news():
    #imports data from Google News Reader and
    #prints top four from each defined topic.
    from gnewsclient import gnewsclient
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

def rss_newsreader():
    #import time
    from datetime import datetime
    import feedparser
    import sys

    rss_feed = ['https://www.aljazeera.com/xml/rss/all.xml',
           'https://hnrss.org/frontpage',
           'https://www.zdnet.com/news/rss.xml']
    total_rss = 3 ##need to make this a variable

    feed_array = []
    rss_cntr = 0
    array_cnt = 0
    entry_loop = 0
    while rss_cntr < total_rss:
        rss_entry = feedparser.parse(rss_feed[rss_cntr])
        e_cnt = len(rss_entry['entries'])
        if e_cnt > 4:
            e_cnt = 4
        while entry_loop < e_cnt:
            feed_entry = rss_entry.entries[entry_loop]
            if feed_entry == None:
                pass
            else:
                feed_array.append(feed_entry)
                array_cnt += 1
            entry_loop += 1
        entry_loop = 0
        rss_cntr += 1
 
    return (feed_array)  
#run once to ensure there is data
rss_newsreader()

def rss_terminal_output(rss_array):
    rss_array = rss_newsreader()
    CGREEN = '\33[32m'
    CEND = '\33[0m'
    CWHITE2 = '\33[97m'
    CGREY = '\33[90m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    import feedparser
    import time
    for rss_entry in rss_array:
        print(CWHITE2 + rss_entry.published + CEND)
        print(CYELLOW2 + "******" + CEND)
        print(CGREY + rss_entry.summary + CEND)
        print(CBLUE2 + "------News Link--------")
        print(CBLUE2 + rss_entry.link + CEND)
        time.sleep(5)
    print(CGREEN + "End of Cycle" + CEND)

 
#Start of the main loop
TICKER=1
while (TICKER != 0):    #because why not?  runs until killed

    read_google_news()

    #generates txt weather report.
    wttr_url="http://wttr.in/stl?2n"
    var_res = requests.get(wttr_url)
    print(var_res.text)
    time.sleep(10)

    #Print the newsfeeds
    import time
    CGREEN = '\33[32m'
    CEND = '\33[0m'

    if (time_reset == 0):
        rss_newsreader()
        time_reset = 1
        later = datetime.now() + timedelta(minutes=31)
        rss_reset_time = later.strftime("%X")
        print(CGREEN + "Refreshing RSS feeds" + CEND)

    rss_array = rss_newsreader()

    rss_terminal_output(rss_array)
    now_time = datetime.now()
    now = now_time.strftime("%X")
    if now > rss_reset_time:
        time_reset = 0
#