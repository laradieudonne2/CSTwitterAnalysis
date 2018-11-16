import pandas as pd
from twitterCollect.tweet import *

tweets=collect_by_user("@EmmanuelMacron")
tweet=tweets[3]

from twitterCollect.sauvegarde_tweet import *

def tweet_le_plus_retweeter(tweets):
    tableau=creer_dataframe_sous_forme_de_tableau(tweets)
    rt_max  = np.max(tableau['RTs'])
    rt  = tableau[tableau.RTs == rt_max].index[0]

    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(tableau['contenu'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(tableau['len'][rt]))

def tweet_avec_le_plus_like (tweets):
    tableau=creer_dataframe_sous_forme_de_tableau(tweets)
    like_max  = np.max(tableau['Likes'])
    rt  = tableau[tableau.RTs == like_max].index[0]

    # Max RTs:
    print("The tweet with more likes is: \n{}".format(tableau['contenu'][rt]))
    print("Number of likes: {}".format(like_max))
    print("{} characters.\n".format(tableau['len'][rt]))

def id_qui_a_le_plus_ecrit(tweets):
    tableau=creer_dataframe_sous_forme_de_tableau(tweets)
    dic={} #on crée un dictionnaire qui va avoir en cle les id et en valeus le nombre de tweets
    for k in range (len(tweets)):
        id=tableau['ID'][k]
        if id in dic: #si la cle existe déjà on rajoute 1
            dic[id]+=1
        else:
            dic[id]=1
    values=dic.values()
    maxi=max(values) #on regarde le max de tweet ecrit
    liste_plus_nombreux=[]
    for cle in dic: #on va retrouver qui a écrit le plus de tweet
        if dic[cle]==maxi:
            liste_plus_nombreux.append(cle)
    return liste_plus_nombreux, len(liste_plus_nombreux)

#print(id_qui_a_le_plus_ecrit(tweets))




def max_nombre_like(tweets):
    list=[]
    for tweet in tweets:
        list.append(tweet.favorite_count)

    maxi=max(list)
    indice_maxi= list.index(maxi)
    return tweets[indice_maxi]

#print(max_nombre_like(tweets))

import textblob
from textblob import *

def analysis_sentiment(tweet):

    mon_tweet=TextBlob(tweet.text) #on garde que le texte du tweet
    return(mon_tweet.sentiment) #on retourne d'abord polarity et ensuite subjectivity


#if __name__ == '__main__':
    #print(analysis_sentiment(tweet))

#import nltk
#nltk.download('punkt')
#nltk.download('wordnet')

def sortir_mots_tweet(tweet):
    mon_tweet=TextBlob(tweet.text)#on garde que le texte du tweet
    words=mon_tweet.words

    for word in words:
        w=Word(word)
        w.lemmatize()
    list=[]
    for mot in words:
        a=mon_tweet.word_counts[mot]
        if a<=1:
            list.append(mot)

    return list


#print(sortir_mots_tweet(tweet))


def analyse_opinion2(tweets):
    positifs=0
    negatifs=0
    neutre=0
    compte=0
    for tweet in tweets:
        compte+=1

        polarity=analysis_sentiment(tweet)[0]
        if polarity>0:
            positifs+=1
        elif polarity<0:
            negatifs+=1
        else:
            neutre+=1
    print("Percentage of positive tweets: {}%".format(positifs*100/compte))
    print("Percentage of neutral tweets: {}%".format(neutre*100/compte))
    print("Percentage de negative tweets: {}%".format(negatifs*100/compte))

#analyse_opinion2(tweets)


