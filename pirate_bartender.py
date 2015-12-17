import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ask_questions():
    answers = {}
    yes = True
    no = False
    
    answer1 = raw_input(questions["strong"])
    if answer1 == 'yes' or answer1 == "Yes":
        answers.update({"strong" : True})
    else:
        answers.update({"strong" : False})
    answer2 = raw_input(questions["salty"])
    if answer2 == 'yes' or answer2 == "Yes":
        answers.update({"salty" : True})
    else:
        answers.update({"salty" : False})
    answer3 = raw_input(questions["bitter"])
    if answer3 == 'yes' or answer3 == "Yes":
        answers.update({"bitter" : True})
    else:
        answers.update({"bitter" : False})
    answer4 = raw_input(questions["sweet"])
    if answer4 == 'yes' or answer4 == "Yes":
        answers.update({"sweet" : True})
    else:
        answers.update({"sweet" : False})
    answer5 = raw_input(questions["fruity"])
    if answer5 == 'yes' or answer5 == "Yes":
        answers.update({"fruity" : True})
    else:
        answers.update({"fruity" : False})
    return answers
    
def make_drink(answers):
    drink = {}
    if answers["strong"] == True:
        drink["strong"] = random.choice(ingredients["strong"])
    if answers["salty"] == True:
        drink["salty"] = random.choice(ingredients["salty"])
    if answers["bitter"] == True:
        drink["bitter"] = random.choice(ingredients["bitter"])
    if answers["sweet"] == True:
        drink["sweet"] = random.choice(ingredients["sweet"])
    if answers["fruity"] == True:
        drink["fruity"] = random.choice(ingredients["fruity"])
    
    return drink
        
if __name__ == '__main__':
    ans = ask_questions()
        
    dr = make_drink(ans)
    print("Here is your drink, this is what is in it: ")
    for ingr in dr:
        print(dr["{}" .format(ingr)])
    
    
    