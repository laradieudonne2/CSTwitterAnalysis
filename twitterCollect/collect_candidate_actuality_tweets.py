
def get_tweets_from_candidates_search_queries(queries, twitter_api):
    list_tweets=[]
    connexion = twitter_api

    for mots in queries: # on fait une requete avec un seul mots clés
        tweets = connexion.search(mots)
        for tweet in tweets:
            list_tweets.append(tweet.text)
            print(tweet.text)

    for k in range (len(queries)-1):
        mots1=queries[0]
        queries=queries[1:] #on supprime à chaque fois le premier pour en avoir plus qu'un.
        for mots_associé in queries:

            tweets = connexion.search(mots1 or mots_associé) #on fait une requete avec deux mots cles
            for tweet in tweets:
                list_tweets.append(tweet.text)
                print(tweet.text)
    return list_tweets

# le or prend si les deux ou un seul des deux mots est là


