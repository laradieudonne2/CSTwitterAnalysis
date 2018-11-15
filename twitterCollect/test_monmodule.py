import unittest
from twitterCollect.twitter_connection_setup import *
from twitterCollect.creer_requete_avec_mots import *
class MonTest (unittest.TestCase):
    def test_fct(self):
        self.assertTrue(type(twitter_setup()),None)

    def test_etape_3_1(self):
        self.assertEqual(get_candidate_queries('num_macron','a.txt'),"rentrer un fichier correct")

if __name__ == '__main__':
    unittest.main()
