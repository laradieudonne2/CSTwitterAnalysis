from twitterCollect.twitter_connection_setup import *
from twitterCollect.APIstreaming import *

def get_replies_to_candidate(num_candidate,date_début=992433028155654144):
    connexion=twitter_setup()
    replies=[]
    #recupere les messages recents du candidat
    statuses = connexion.user_timeline(id = num_candidate, language="fr",rpp=100)
    for full_tweet in statuses:

       #query pour retrouver des tweets repondant a l'utilisateur num_candidate

        query = 'to:'+ str(num_candidate)
        print (full_tweet)
        for tweet in connexion.search(q=query, since_id=date_début, result_type='recent',timeout=999999):

            #si le tweet renvoye par la requete possede un champs "in reply_to__status_id_str" cest a dire si cest une reponse a un tweet

           if hasattr(tweet, 'in_reply_to_status_id_str'):
                # si c'ets une reponse au tweet actuel (full_tweet) du candidat
               if (tweet.in_reply_to_status_id_str==full_tweet.id_str):
                   replies.append(tweet.text)
                   print(tweet.text)
    return replies

def get_retweets_of_candidate(num_candidate, date_debut=992433028155654144):
    connexion=twitter_setup()
    retweet=[]
    #recupere les messages recents du candidat
    statuses = connexion.user_timeline(id = num_candidate, language="fr",rpp=100)
    for full_tweet in statuses:

       #query pour retrouver des tweets repondant a l'utilisateur num_candidate

        query = 'to:'+str(num_candidate)
        print (full_tweet.text)
        for tweet in connexion.search(q=query, since_id=date_debut, result_type='recent',timeout=999999):

           if hasattr(tweet, 'retweeted_status'):
                if (tweet.retweeted_status_id_str==full_tweet.id_str):
                    retweet.append(tweet.text)
                    print(tweet.text)
    return retweet

get_replies_to_candidate(1976143068)
#get_retweets_of_candidate(1976143068) # num d'Emmanuel Macron

def collect_en_temps_reel(num_candidate):
    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(id==num_candidate or stream.retweeted_status_id_str==num_candidate)

#collect_en_temps_reel(1976143068)



