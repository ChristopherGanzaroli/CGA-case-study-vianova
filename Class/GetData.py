import json
import requests

class GetAPIData:
    """
    Class récupération data
    """
    
    def __init__(self, url):                # url recupérée lors de l'initialisation de l'objet
        self.url = url

###################################################################################################
##   Récupération des données au format json                                                     ##
###################################################################################################
    def json_data(self):
        r = requests.get(self.url)
        json_data = r.json()
        return json_data
