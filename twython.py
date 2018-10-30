from twython import Twython
import pandas as pd

#Log in Twitter API
TWITTER_APP_KEY = "bgAsjeaOjDhijVVNj0CKvmXd1"
TWITTER_APP_KEY_SECRET = "i4ogIK1Pw0sHtPMve71JgzONGGz5osFNoKELQ31QmXdJZK6CJF"
TWITTER_ACCESS_TOKEN = "946009581813039106-1p9P45cWrcjhgugctlTA48VzkxkoKxT"
TWITTER_ACCESS_TOKEN_SECRET = "CXF8ijxLrF4T9KHXsNR8XhJx77uKARW9KGS0PtrOeYa4j"

t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

#Query
term = 'Xiaomi'
tweet_metadatas = t.search(q=term,count=20,result_type='recent',lang='id')

#Scrapping
data_list = []
for tweet in tweet_metadatas['statuses']:
    meta = dict()
    meta['tweet'] = tweet['text']
    meta['timestamp'] = tweet['created_at']
    meta['username'] = tweet['user']['screen_name']
    
    data_list.append(meta)
    
#Visual
data = pd.DataFrame(data_list)
data.head()

#Export
writer = pd.ExcelWriter('result.xlsx')
data.to_excel(writer,'Sheet1',index=False)
writer.save()