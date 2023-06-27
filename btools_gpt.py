##################################################################
# B-TOOLS-GPT v0.24
#
# GPT:
# gpt(prompt (req), model, messages, temperature, top_p, presence_penalty, frequency_penalty, user)  - OpenAI API (Paid)
#
##################################################################

import time
import openai

openai.api_key = os.environ["OPENAI_API_KEY"]

def gpt(prompt, model="gpt-3.5-turbo", messages=None, temperature=None, top_p=None, presence_penalty=None, frequency_penalty=None, system=None):
    
    delay = 5  # Initial retry delay in seconds (used in case of server error/failure) 

    # Clamp presence_penalty between -2 and 2
    presence_penalty = min(max(presence_penalty, -2), 2) if presence_penalty is not None else 0.0

    # Clamp frequency_penalty between -2 and 2
    frequency_penalty = min(max(frequency_penalty, -2), 2) if frequency_penalty is not None else 0.0

    # Clamp top_p between 0.0 and 1.0
    top_p = min(max(top_p, 0.0), 1.0) if top_p is not None else 1.0

    # Clamp temperature between 0.0 and 2.0
    temperature = min(max(temperature, 0.0), 2.0) if temperature is not None else 1.0

    # Create the message log if none was provided
    if messages is None:
        messages = []
        # Append the system role if specified
        if system is not None:
            messages.append({"role": "system", "content": system})
        else:
            messages.append({"role": "system", "content": "You are an expert."})

    # Otherwise, use the provided message log
    else:
        if system is not None:
            # Update the provided system role
            for message in messages:
                if message.get("role") == "system":
                    message["content"] = system
                    break

    # Append the prompt to the message log
    messages.append({"role": "user", "content": prompt})

    error_count = 0

    while True:
        try:
            # Try to connect
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                temperature=temperature,
                top_p=top_p,
                presence_penalty=presence_penalty,
                frequency_penalty=frequency_penalty
            )

            print(str(response))

            # Parse the JSON string into a Python object    
            content = response['choices'][0]['message']['content']
            break  # If successful, exit the loop

        except Exception as e:
            if error_count > 99:
                return None
            else:                    
                # If the error is caused by 4K maximum context, switch to 16K.
                if str(e).__contains__("This model's maximum context length is"):
                    print("Trying larger context. Error: " + str(e))
                    model = "gpt-3.5-turbo-16k-0613"
                    error_count = 100 # If we've raised the context size but we're still returning above the maximum, the request will never succeed. Prepare to abort.
                else:
                    print("Connection failed with error: " + str(e) + ", retrying in {} seconds...".format(delay))
                    time.sleep(delay)  # Wait for the specified delay
                    delay *= 2  # Double the delay for the next attempt
                    error_count += 1 # Increment error count (We'll abort at 100)
                    if delay > 600:  # If the delay exceeds 10 minutes, reset it to 10 minutes
                        delay = 600
    return str(content)
