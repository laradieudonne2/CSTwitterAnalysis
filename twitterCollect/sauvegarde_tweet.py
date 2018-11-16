import json
import tweepy
from twitterCollect.tweet import *

tweets=collect_by_user("@EmmanuelMacron")
tweet=tweets[0]

def store_tweets(tweets,filename):
    list_tweet=[]
    for tweet in tweets:
        creation_dic={}
        creation_dic["id"]=tweet.id
        creation_dic["id.str"]=tweet.id_str
        creation_dic["created_at"]=str(tweet.created_at)
        creation_dic["text"]=tweet.text
        list_tweet.append(creation_dic)

    with open(filename+ ".json", "w") as write_file:
        json.dump(list_tweet, write_file)


#store_tweets(tweets,"essai2")


def store_tweets_text(tweets,filename): #on a que le text sous forme de string dans le fichier.

    with open(filename+ ".json", "a", encoding='utf8') as write_file:

        for tweet in tweets:
            json.dump(tweet.text, write_file, ensure_ascii=False)


import pandas as pd

def creer_datframe_a_partir_tweet(tweet):
    s=pd.Series ([tweet.id,tweet.id_str,tweet.text,str(tweet.created_at)]) #on garde que les données necessaires
    return s

#print (creer_datframe_a_partir_tweet(tweet))
import ast
def creer_dataframe_a_partir_fichier(fichier):
    mon_fichier=open(fichier,'r')
    list_dataframe=[]
    tweets=json.load(mon_fichier)
    print(type(tweets[0]))
    print(tweets[0])
    for dict in tweets:
        s=pd.Series([dict["id"],dict["id.str"]])
        print(s)
    return list_dataframe

#creer_dataframe_a_partir_fichier("essai2.json")

import numpy as np
def creer_dataframe_sous_forme_de_tableau(tweets):

   tableau = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['contenu'])
   #on rajoute des colommnes à notre tableau
   tableau['len']  = np.array([len(tweet.text) for tweet in tweets])
   tableau['ID']   = np.array([tweet.id for tweet in tweets])
   tableau['Date'] = np.array([tweet.created_at for tweet in tweets])
   tableau['Source'] = np.array([tweet.source for tweet in tweets])
   tableau['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
   tableau['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
   return tableau


#print(creer_dataframe_sous_forme_de_tableau(tweets))

#tableau=creer_dataframe_sous_forme_de_tableau(tweets)
#print([str(tableau['Date'][k]) for k in range(len(tweets))])
