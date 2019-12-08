# functions that appends the user input text into dictionary
# Knows that if sentence starts with interrogative, to put question mark at the end.

def exercise(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "%s?" %(phrase.capitalize())
    else:
        return "%s." %(phrase.capitalize())

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "/end":
        break
    else:
        results.append(exercise(user_input))

print(results)