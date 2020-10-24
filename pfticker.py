import gnewsclient
from gnewsclient import gnewsclient
import time

TTOPICS = ['technology', 'business', 'world', 'nation', 'sport']
CWHITE =  '\33[37m'
CCYAN = '\33[36m'
CGREEN = '\33[32m'
CEND = '\33[0m'
CWHITE2 = '\33[97m'
CBLUE2 = '\33[94m'

ticker=1
while (ticker != 0):
    for TTOPIC in TTOPICS:
        client = gnewsclient.NewsClient(language='english',
                                location='United States',
                                topic=TTOPIC,
                                max_results=3)

        news_list = client.get_news()

        for item in news_list:
            print(CWHITE2 + "Title : ", item['title'] + CEND)
            print(CBLUE2 + "Link : ", item['link'] + CEND)
            print("")

        time.sleep(6)

print (CGREEN + "End of Cycle" + CEND)


#Black: \u001b[30m.
#Red: \u001b[31m.
# #Green: \u001b[32m.
#Yellow: \u001b[33m.
#Blue: \u001b[34m.
#Magenta: \u001b[35m.
#Cyan: \u001b[36m.
#White: \u001b[37m.
