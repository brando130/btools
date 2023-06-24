##################################################################
# B-TOOLS-NET v0.24
#
# Net:
# GetHTML(url)
#
##################################################################

import requests

def GetHTML(url):

    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Get the HTML content of the response
    html_content = response.text

    # Print the HTML content
    return html_content