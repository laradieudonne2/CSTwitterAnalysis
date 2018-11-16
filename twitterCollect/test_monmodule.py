import unittest
from twitterCollect.twitter_connection_setup import *
from twitterCollect.tweet import *
from twitterCollect.creer_requete_avec_mots import *
from twitterCollect.sauvegarde_tweet import *

class MonTest (unittest.TestCase):
    def test_fonction_connexions(self):
        self.assertTrue(type(twitter_setup()),None)

    def test_tweet(self):
        self.assertTrue(type(collect()),None)
        self.assertEqual(collect_by_user("@BarbierHeloise"),[])
        self.assertEqual(type(collect_by_user("@EmmanuelMacron")),tweepy.models.ResultSet)

    def test_fonction_sauvegarde_tweets(self):
        self.assertTrue(type(twitter_setup()),None)

    def test_etape_3_1(self):
        self.assertEqual(get_candidate_queries('num_macron','a.txt'),"rentrer un fichier correct")

if __name__ == '__main__':
    unittest.main()
