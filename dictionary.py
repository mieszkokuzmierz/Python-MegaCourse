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
    elif w.upper() in data: #as there are some words like USA, NATO which are all in capital letters
        return data[w.upper()]
    #adding get_close_matches functionality to add the words that can be found even if typo (e.g. for rainn it will ask if you meant rain instead)
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Press Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn =="N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."

    else:
        return "The word doesn't exist. Please double check it."
 
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

