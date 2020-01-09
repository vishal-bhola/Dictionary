import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        decide="y"
        while decide!="n":
            print("\nHey, Did you mean %s instead ?" %get_close_matches(word,data.keys())[0])
            print("Press y for Yes or n for No",end=' ')
            decide=input()
            if decide == "y":
                return data[get_close_matches(word,data.keys())[0]]
            elif decide =="n":
                print("\n🔥 Buddy have entered a wrong word please check it again!!!\n")
            else:
                print("You have entered wrong input please enter y or n")   
    else:
        print("\n🔥 Buddy have entered a wrong word please check it again!!!\n")


word="start"
while(word!="n"):
    print("Enter the word you want to search (Type n to exit):-",end=' ' )
    word = input()
    if word!="n":
        meanings = translate(word)
        if type(meanings)==list:
            print("\nMeanings:-")
            index=1
            for meaning in meanings:
                print( str(index) + " " + meaning)
                index+=1
        print("---------------------------------------------------------------\n")        
    else:
        print("Thanks for Surfing 😇")           


