import json
from tkinter import *
from tkinter.messagebox import showinfo,askquestion
from difflib import get_close_matches


data = json.load(open("data.json"))


win = Tk()
win.title("Online Dictionary")
win.geometry('300x150')


def translate():
    word=entry.get()
    word = word.lower()
    if word in data:
        meanings = data[word]
    elif word.title() in data:
        meanings = data[word.title()]
    elif word.upper() in data:
        meanings = data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        decide = askquestion("Meanings:-","\nHey, Did you mean '%s' instead ?" %get_close_matches(word,data.keys())[0],icon="info")
        if decide == "yes":
            meanings = data[get_close_matches(word,data.keys())[0]]
        else :
            showinfo("OOPS","Then, Buddy you have entered a wrong word please check it again!!!\n")
    else:
        showinfo( "OOPS","That's not a correct word please check it again!!!\n")
    if type(meanings)==list:
            index=1
            result=""
            for meaning in meanings:
                result+=( str(index) + ". " + meaning)
                index+=1
                result+="\n\n"
            showinfo("\nMeanings:-",result)    


label=Label(win,text="Enter Your Word:- ")
label.grid(row=2,column=1)

entry = Entry(win)
entry.grid(row=2,column=5)

button=Button(win,text="Search",command=translate)
button.grid(row=3,column=5)


win.mainloop()