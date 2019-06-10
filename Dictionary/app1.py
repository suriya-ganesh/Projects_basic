import json
from appJar import *
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data :
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        app.clearTextArea("outputtextarea")
        app.setTextArea("outputtextarea","You meant %s instead? Press Yes or No: " % get_close_matches(w, data.keys())[0])
        return ""
    else:
        return "The word doesn't exist. Please double check it once."


app = gui()
app.setSize("800x300")
def press(button):
    if button == "Submit":
        app.clearTextArea("outputtextarea")
        word = app.getEntry("Enter Word:")
        word = str(word)
        output = translate(word)
        displayresult(output)
    else:
        app.stop()

def displayresult(output):
    result = ""
    if type(output) == list:
        for item in output:
            print("meaning: ", item)
            result = result + "\n" + item
        app.clearTextArea("outputtextarea")
        app.setTextArea("outputtextarea", result)
    elif output == "":
        print("waiting for yes or no press")
    else:
        print("meaning: ", output)
        app.clearTextArea("outputtextarea")
        app.setTextArea("outputtextarea", output)

def additionalquestion(button):
    word = app.getEntry("Enter Word:")
    if button == "Yes":
        app.setEntry("Enter Word:",get_close_matches(word, data.keys())[0])
        output = data[get_close_matches(word, data.keys())[0]]
    else:
        output = "The word doesn't exist. Please double check it."
    displayresult(output)

with app.frame("word",row=0, column=0, bg='cyan', sticky='NEW', stretch='COLUMN'):
    app.addLabelEntry("Enter Word:")
    app.addButtons(["Submit", "cancel"],press)
    app.addTextArea("outputtextarea",text="")
with app.frame("additionalquestion", row=1, column = 0, bg = 'white'):
    app.addButtons(["Yes","No"],additionalquestion)


app.go()
