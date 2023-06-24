##################################################################
# B-TOOLS-GPT4FREE v0.24
#
# GPT4FREE:
# gpt_you(prompt) - GPT4FREE (Limited, unreliable, wysiwyg)
#
##################################################################

import gpt4free
from gpt4free import Provider
import time

def gpt_you(prompt):
    delay = 5  # Initial retry delay in seconds (used in case of server error/failure) 
    while True:
        try:
            # Try to connect
            content = gpt4free.Completion.create(Provider.You, prompt=prompt) 
            break  # If successful, exit the loop

        except:
            print("Connection failed, retrying in {} seconds...".format(delay))
            time.sleep(delay)  # Wait for the specified delay
            delay *= 2  # Double the delay for the next attempt
            if delay > 600:  # If the delay exceeds 10 minutes, reset it to 10 minutes
                delay = 600
    return str(content)
