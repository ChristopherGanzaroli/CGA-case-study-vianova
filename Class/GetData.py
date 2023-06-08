import json
import requests

class GetAPIData:
    """
    This class retrieves the data in json format from api
    """
    
    def __init__(self, url): # API url
        self.url = url

###################################################################################################
##                          GET API DATA JSON FORMAT                                             ##
###################################################################################################
    def json_data(self):
        r = requests.get(self.url)
        json_data = r.json()
        return json_data