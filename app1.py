import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("did you mean %s instead? if yes enter Y if no enter N :"% get_close_matches(w,data.keys())[0])
        if yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        if yn=="n":
            return "The word does'nt exist plz check it"
        else:
            return"we didn't understand your entry"
    else:
        return"The word dos'nt exist,plz check it"

word=input("enter word: ")
output= translate(word)

if output==list:
    for item in output:
        print(item)
else:
    print(output)
