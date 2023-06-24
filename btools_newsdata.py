##################################################################
# B-TOOLS-NEWSDATA v0.24
#
# NewsData.io API:
# latest_news(query (string - optional)) - returns a JSON object with current weather
#
##################################################################

import requests
import os

def latest_news(query=""):

    API_KEY = os.environ["NEWSDATA_API_KEY"]
    url = f'https://newsdata.io/api/1/news?apikey={API_KEY}&q={query}'
    if query == "":
        url = f'https://newsdata.io/api/1/news?apikey={API_KEY}'        

    response = requests.get(url)
    data = response.json()

    return data