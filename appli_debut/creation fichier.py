import json

from twitterCollect.tweet import *
tweets=collect_by_user("@EmmanuelMacron")

def store_tweets_text(tweets,filename):

    with open(filename+ ".json", "a", encoding='utf8') as write_file:

        for tweet in tweets:
            json.dump(tweet.text, write_file, ensure_ascii=False)


store_tweets_text(tweets,"mots_tweets")


