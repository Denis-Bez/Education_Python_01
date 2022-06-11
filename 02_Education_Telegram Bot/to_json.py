import json

ar = []

with open('cenz.txt', encoding='utf-8') as words:
    for word in words:
        word = word.lower().split('\n')[0]
        if  word != '':
            ar.append(word)

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)