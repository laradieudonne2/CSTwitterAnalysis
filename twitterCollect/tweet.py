

from twitterCollect import twitter_connection_setup

def collect():
    connexion = twitter_connection_setup.twitter_setup()
    tweets = connexion.search("Emmanuel" or "Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)


#collect()

def collect_by_user(user_id):
    connexion = twitter_connection_setup.twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    #for status in statuses:
        #print(status)
    return statuses

collect_by_user("@EmmanuelMacron")
