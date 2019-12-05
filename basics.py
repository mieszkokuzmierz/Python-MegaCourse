def zmiana(zdanie):
    questions = ("how", "what", "why")
    wielka = zdanie.capitalize()
    if zdanie.startswith(questions):
        return "%s?" % zdanie.format(wielka)
    else:
        return "%s." % zdanie.format(wielka)


lista = []
while True:
    tekst = input("Say something (/end ends session): ")
    if tekst == "/end":
        break
    else: lista.append(zmiana(tekst))


print(" ".join(lista)))

#adding comments to the file

