import json
from difflib import get_close_matches

data = json.load(open("7data.json")) #loading the data in a json format. data was gotten from the internet

def definition(word):
    word = word.lower() #converts the word to lowercase before anything
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0: #if > 0, then there is a similar item.
        yn = input("Did you mean '%s' instead? Enter Y if 'yes' or n if 'No': " % get_close_matches(word, data.keys())[0])
        if yn == "Y": #this is done because we want a smart program that can ensure the code doesnt break
            return data[get_close_matches(word, data.keys())[0]] #returns the value of the first key whuch was suggested by the get_close_matches function
        elif yn =="n":
            return "This word does not exist "
        else:
            return "We don't understand your response. "
    else:
        return "This word does not exist "

word = input("Enter new word: ") #the input statement that takes in word from the user


output = (definition(word))

if type(output) == list:
    for item in output:
        print(item)
else:
        print(output)
