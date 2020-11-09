#To dos
# bring the site variables outside the function
# make the site count variable measure the array
#create another function to ingest site recommendations
#make the output a separate function so it can be redirected to a web function
# create a web function for the output

var_rss = ['https://www.aljazeera.com/xml/rss/all.xml',
           'https://hnrss.org/frontpage',
           'https://www.zdnet.com/news/rss.xml']


def rss_newsreader():
    #import time
    from datetime import datetime
    import feedparser
    import sys

    rss_feed = ['https://www.aljazeera.com/xml/rss/all.xml',
                'https://hnrss.org/frontpage',
                'https://www.zdnet.com/news/rss.xml']
    total_rss = 3 ##need to make this a variable
    rss_reset = 0

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
    rss_reset = datetime.now()
 
    return (feed_array, rss_cntr)  

def rss_terminal_output():
    rss_array, rss_cnt = rss_newsreader()
    CGREEN = '\33[32m'
    CEND = '\33[0m'
    CWHITE2 = '\33[97m'
    CBLUE2 = '\33[94m'
    CGREY = '\33[90m'
    CYELLOW2 = '\33[93m'
    import feedparser
    import time
    entry_no = 0
    while entry_no < rss_cnt:
        entry = rss_array[entry_no]
        print(CWHITE2 + entry.published + CEND)
        print(CYELLOW2 + "******" + CEND)
        print(CGREY + entry.summary + CEND)
        print(CBLUE2 + "------News Link--------")
        print(CBLUE2 + entry.link + CEND)
        time.sleep(5)
        print(CGREEN + "End of Cycle" + CEND)
        entry_no += 1


   ###make the 31-minute timer a separate function
#time_reset goes at top of script, before initial loop
from datetime import datetime, timedelta
time_reset = 0
rss_reset_time = datetime.now() + timedelta(minutes=31)
#top of the loop
current_time = datetime.now()

## end of top-of-script portion

#Print the newsfeeds
import time
CGREEN = '\33[32m'
CEND = '\33[0m'

while (time_reset == 0):
    rss_newsreader()
    time_reset = 1
    rss_reset_time = datetime.now() + timedelta(minutes=31)

rss_array, rss_ctr = rss_newsreader()
if time_reset == 1:
    print(CGREEN + "Refreshing RSS feeds" + CEND)
else:
    print(CGREEN + "Recycling RSS feeds" + CEND)
rss_terminal_output(rss_array,rss_ctr)
if (current_time >= rss_reset_time):
    time_reset = 0

