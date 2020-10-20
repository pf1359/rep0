import gnewsclient
from gnewsclient import gnewsclient
tclient = gnewsclient.NewsClient(language='english', location='United States', topic='Technology', max_results=5)

tclient.get_config()


#>> > client.topics
#['Top Stories',
 #'World',
 #'Nation',
 #'Business',
# 'Technology',
#'Entertainment',
 #'Sports',
 #'Science',
# 'Health']
