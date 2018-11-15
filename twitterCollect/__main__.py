from twitterCollect.tweet_collection import *
from twitterCollect.twitter_connection_setup import *


twitterAPI=twitter_setup()

def ensemble_des_tweets(num_candidate, file_path,twitterAPI):
    liste1=collection_des_tweets_a_partir_dun_tweet_du_candidat(num_candidate)
    liste2=collection_des_tweets_à_partir_mots_cles(num_candidate, file_path,twitterAPI)
    return liste1+liste2

