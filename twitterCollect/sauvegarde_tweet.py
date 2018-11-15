import json

from twitterCollect.collect_candidate_tweet_activity import *
tweets= get_replies_to_candidate(1976143068)

def store_tweets(tweets,filename):
    with open(filename+ ".json", "w") as write_file:
        json.dump(tweets, write_file)


store_tweets(tweets,"essai1")
