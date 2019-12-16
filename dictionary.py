#First app from Ardit Sulce's Udemy Course
#Already created .json file containng dictionaries of english words uploaded into Python code
#Code searches through dictionary, returns its meaning, can go through minor typos and distinguish them, not giving errors

import json
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word doesn't exist. Please check."

word = input("Enter the word: ")

print(translate(word))
