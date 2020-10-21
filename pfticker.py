import gnewsclient
from gnewsclient import gnewsclient
import time

ticker=1
while (ticker != 0):
    client2 = gnewsclient.NewsClient(language='english',
                                location='United States',
                                topic='technology',
                                max_results=5)

    news_list = client2.get_news()

    for item in news_list:
        print("Title : ", item['title'])
        print("Link : ", item['link'])
        print("")

    time.sleep(10)
    client3 = gnewsclient.NewsClient(language='english',
                                location='United States',
                                topic='business',
                                max_results=5)

    news_list = client3.get_news()

    for item in news_list:
        print("Title : ", item['title'])
        print("Link : ", item['link'])
        print("")

    time.sleep(10)
    client4 = gnewsclient.NewsClient(language='english',
                                location='United States',
                                topic='world',
                                max_results=5)

    news_list = client4.get_news()

    for item in news_list:
        print("Title : ", item['title'])
        print("Link : ", item['link'])
        print("")

    time.sleep(10)
    client5 = gnewsclient.NewsClient(language='english',
                                location='United States',
                                topic='nation',
                                max_results=5)

    news_list = client5.get_news()

    for item in news_list:
        print("Title : ", item['title'])
        print("Link : ", item['link'])
        print("")

    time.sleep(10)

    client6 = gnewsclient.NewsClient(language='english',
                                location='United States',
                                topic='sports',
                                max_results=5)

    news_list = client6.get_news()

    for item in news_list:
        print("Title : ", item['title'])
        print("Link : ", item['link'])
        print("")

    time.sleep(10)
print("End of Cycle")