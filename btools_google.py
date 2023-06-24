##################################################################
# B-TOOLS-GOOGLE v0.24
#
# Google:
# google(query (string)) - returns a Google CSE (Custom Search Engine) JSON object - rtfm (hint: print(json.dumps(data, indent=4)) )
#
##################################################################

import requests
import os

def google(query):

    API_KEY = os.environ["GOOGLE_API_KEY"]
    SEARCH_ENGINE_ID = os.environ["GOOGLE_SEARCH_ENGINE_ID"]

    url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}'

    response = requests.get(url)
    data = response.json()

    return data