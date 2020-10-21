from gnewsclient import gnewsclient

client = gnewsclient.NewsClient(language='english',
                                location='United States',
                                topic='technology',
                                max_results=3)

news_list = client.get_news()

for item in news_list:
    print("Title : ", item['title'])
    print("Link : ", item['link'])
    print("")
