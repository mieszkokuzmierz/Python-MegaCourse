#First app from Ardit Sulce's Udemy Course
#Already created .json file containng dictionaries of english words uploaded into Python code
#Code searches through dictionary, returns its meaning, can go through minor typos and distinguish them, not giving errors

import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #as there are some names like capitals in capital letters, we need to make sure it finds these as well.
        return data[w.title()]
    else:
        return "The word doesn't exist. Please double check it."
 
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)