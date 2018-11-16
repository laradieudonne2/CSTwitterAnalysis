import pandas as pd
from twitterCollect.tweet import *
import matplotlib.pyplot as plt

tweets=collect_by_user("@EmmanuelMacron")
tweet=tweets[3]

from twitterCollect.sauvegarde_tweet import *

data=creer_dataframe_sous_forme_de_tableau(tweets)
tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
tret = pd.Series(data=data['RTs'].values, index=data['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

plt.show()
