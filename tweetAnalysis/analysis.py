import pandas as pd
from twitterCollect.tweet import *
tweets=collect_by_user("@EmmanuelMacron")

def max_nombre_like(tweets):
    list=[]
    for tweet in tweets:
        list.append(tweet.favorite_count)

    maxi=max(list)
    indice_maxi= list.index(maxi)
    return tweets[indice_maxi]

#print(max_nombre_like(tweets))

import matplotlib
import matplotlib.pyplot as plt
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()

import textblob
