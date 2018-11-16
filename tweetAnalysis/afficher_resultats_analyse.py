from twitterCollect.sauvegarde_tweet import *
from twitterCollect.tweet import *

tweets=collect_by_user("@EmmanuelMacron")
tableau=creer_dataframe_sous_forme_de_tableau(tweets)

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", context="talk")
rs = np.random.RandomState(1) #je vois pas à quoi ça sert

# Set up the matplotlib figure
f, (ax1) = plt.subplots(1, 1, figsize=(7, 5), sharex=True)

# Generate some retweets data
#x = np.array([str(tableau['Date'][k]) for k in range(len(tweets))])
x = np.array([k for k in range(5)])
y1 = np.array([tableau['Likes'][k] for k in range(5)])

sns.barplot(x=x, y=y1, palette="rocket", ax=ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Likes")

# Finalize the plot
sns.despine(bottom=True)
plt.setp(f.axes, yticks=[])
plt.tight_layout(h_pad=2)
plt.show()



