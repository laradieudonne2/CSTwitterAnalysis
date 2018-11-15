from twitterCollect import twitter_connection_setup
from twitterCollect.sauvegarde_tweet import *
from pytest import *


def test_collect():
    tweets = twitter_connection_setup.twitter_setup()
    data =  creer_datframe_a_partir_tweet(tweets)
    assert 'tweet_textual_content' in data.columns

import coverage
import pytest.cov
