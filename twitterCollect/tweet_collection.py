from twitterCollect.APIstreaming import *
from twitterCollect.collect_candidate_actuality_tweets import *
from twitterCollect.collect_candidate_tweet_activity import *
from twitterCollect.tweet import *
from twitterCollect.creer_requete_avec_mots import *
from twitterCollect.tweet_collection import *
from twitterCollect.twitter_connection_setup import *

def collection_des_tweets_à_partir_mots_cles(num_candidate, file_path,twitterAPI):
    liste_mots_cles=get_candidate_queries(num_candidate,file_path)
    liste_tweet=get_tweets_from_candidates_search_queries(liste_mots_cles,twitterAPI)
    return liste_tweet

def collection_des_tweets_a_partir_dun_tweet_du_candidat(num_candidate):
    liste_des_réponses=get_replies_to_candidate(num_candidate)
    liste_des_retweet=get_retweets_of_candidate(num_candidate)
    return liste_des_retweet+liste_des_réponses
