import json
import tweepy
from twitterCollect.tweet import *

tweets=collect_by_user("@EmmanuelMacron")
tweet=tweets[0]
#print(tweet)
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

creer_dataframe_a_partir_fichier("essai2.json")
