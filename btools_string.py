##################################################################
# B-TOOLS-STRING v0.24
#
# String:
# GetStringsBetween(string, opening, close)
# GetRight(string, div)
# GetLeft(string, div)
# write(path, content) - Read txt from file
# read(path) - Write txt to file
# Wild2Reg(wildcard) - Input wildcard, Output RegEx
# WildcardMatch() - Utility function used by Wild2Reg()
# truncate(text, size) - Truncate to the final n characters (size = int)
#
##################################################################

import os
import re

def GetStringsBetween(input_str, opening, close):
    result = []
    start = input_str.find(opening)
    while start != -1:
        end = input_str.find(close, start + len(opening))
        if end == -1:
            break
        result.append(input_str[start + len(opening):end])
        start = input_str.find(opening, end + len(close))
    return result

def GetLeft(input_str, character):
    index = input_str.find(character)
    if index == -1:
        return input_str
    return input_str[:index]

def GetRight(input_str, character):
    index = input_str.find(character)
    if index == -1:
        return input_str
    return input_str[index+len(character):]

def write(path, content, append=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    mode = "a" if append else "w"
    with open(path, mode, encoding="utf-8") as f:
        f.write(str(content) + "\n")
        # print(str(content) + "\n")

def read(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    return content

def Wild2Reg(input):
    # Replace ? with . (any single character wildcard)
    input = input.replace('?', '.')
    # Replace * with .* (any multiple character wildcard)
    input = input.replace('*', '.*')
    # Enclose the input string in ^ and $ (match the whole string)
    #input = '^' + input + '$'
    return input

def WildcardMatch(input, search):
    # Convert the input wildcard to a regex pattern
    pattern = Wild2Reg(search)
    # Search for the pattern in the input string
    match = re.search(pattern, input)
    if match:
        # Return the matched substring
        return match.group(0)
    else:
        # No match found
        return None

def truncate(input, size):
    # Check if the input string is already under n characters
    if len(input) <= size:
        return input

    # Find the last occurrence of a new line character within the final n characters
    last_newline_index = input[-size:].rfind('\n')

    # If a new line character is found within the final n characters, return the string from that index onwards
    if last_newline_index != -1:
        return input[last_newline_index+1:]
    
    # If no new line character is found, return the final n characters
    return input[-size:]