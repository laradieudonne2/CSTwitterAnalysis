
from twitterCollect import twitter_connection_setup





def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:

        motscles=open(file_path) #on ouvre le fichier
        monfichier=motscles.read() #on lit le fichier ce qui permet de la parcourir ensuite
        Liste_mots_cles=[]
        for mots in monfichier:
            Liste_mots_cles.append(mots)

        return Liste_mots_cles

    except FileNotFoundError:
        return("rentrer un fichier correct")



#get_candidate_queries(1,"a")

#on aurait pu utliser la fonction product
