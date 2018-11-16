import multidict as multidict

import numpy as np
import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        #on enlève tous les mondes qui se répète beaucoup en français et qui sont inintéressant
        if re.match("a|la|la|sur|à|dans|et|du|en|de|les|qui|nos|tout|tous|que|ne|ont|pour|parce|c'est|se|the|ce|pas|to|plus|of|est|we|son|is|je|leur|par|sont|on|y|faire|fait|faut|n'est|l|l'|où|n'y|fait|faut|n'est|sommes|qu'il|nous|étais", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict


def makeImage(text):
    alice_mask = np.array(Image.open(r"C:\Users\Lara DIEUDONNE\Pictures\PochetteCDcommus\twitter_mask.png"))

    wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
    # generate word cloud
    wc.generate_from_frequencies(text)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'mots_tweets.json'), encoding='utf-8')
text = text.read()
makeImage(getFrequencyDictForText(text))

