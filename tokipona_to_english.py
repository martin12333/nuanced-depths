<<<<<<< HEAD
# Run with Python 3
# py -3
=======
# Will be merged and migrated to a module shortly
>>>>>>> 48ba035aae5ea3e996ea8c0002fe7fbd80e4ea3b

# the toki pona dictionary as simple as I could make it!

tpdictionary = {
'a': 'ah!',
'akesi': 'reptile',
'ala': 'none',
'alasa': 'gather',
'ale': 'all',
'anpa': 'under',
'ante': 'different',
'anu': 'or',
'awen': 'wait',
'e': 'the',
'en': 'and',
'esun': 'shop',
'ijo': 'thing',
'ike': 'bad',
'ilo': 'tool',
'insa': 'inside',
'jaki': 'yucky',
'jan': 'person',
'jelo': 'yellow',
'jo': 'have',
'kala': 'fishy',
'kalama': 'make noise',
'kama': 'come',
'kasi': 'leaf',
'ken': 'can',
'kepeken': 'use',
'kili': 'fruit',
'kin': 'also',
'kipisi': 'cut',
'kiwen': 'hard stone',
'ko': 'squishy',
'kon': 'wind/smell/soul',
'kule': 'colour',
'kulupu': 'club',
'kute': 'listen',
'la': 'it is *goes between phrase of context and sentence*',
'lape': 'sleep',
'laso': 'blue-green',
'lawa': 'head',
'len': 'clothes',
'lete': 'cold',
'li': 'is',
'lili': 'little',
'linja': 'line',
'lipu': 'paper',
'loje': 'red',
'lon': 'here',
'luka': 'hand (or five if counting numbers)',
'lukin': 'look at',
'lupa': 'hole',
'ma': 'land',
'mama': 'parent',
'mani': 'money',
'meli': 'female',
'mi': 'me',
'mije': 'man',
'moku': 'food',
'moli': 'death',
'monsi': 'behind',
'mu': 'moo!',
'mun': 'moon',
'musi': 'recreation',
'mute': 'many',
'namako': 'embellish',
'nanpa': 'number',
'nasa': 'crazy',
'nasin': 'way',
'nena': 'hill or nose',
'net': 'Internet',
'ni': 'this',
'nimi': 'name',
'noka': 'leg or foot',
'o': 'hey!',
'oko': 'eye',
'olin': 'love',
'ona': 'they',
'open': 'open',
'pakala': 'accident',
'pali': 'work',
'palisa': 'stick',
'pan': 'carbohydrate',
'pana': 'give',
'pi': 'of',
'pilin': 'feeling',
'pimeja': 'dark',
'pini': 'end',
'pipi': 'bug',
'poka': 'next to',
'poki': 'bowl',
'pona': 'good',
'pu': 'The Official toki pona Book',
'sama': 'same',
'seli': 'heat',
'selo': 'outside',
'seme': 'what',
'sewi': 'above',
'sijelo': 'body',
'sike': 'circle',
'sin': 'new',
'sina': 'you',
'sinpin': 'front or wall',
'sitelen': 'picture or writing',
'sona': 'know',
'soweli': 'land animal',
'suli': 'big',
'suno': 'sun',
'supa': 'flat surface',
'suwi': 'sweet',
'tan': 'from',
'taso': 'only or but',
'tawa': 'towards',
'telo': 'liquid',
'tenpo': 'time',
'toki': 'communication',
'tomo': 'house',
'tu': 'two',
'unpa': 'sex',
'uta': 'mouth',
'utala': 'conflict',
'walo': 'white',
'wan': 'one',
'waso': 'birdy',
'wawa': 'power',
'weka': 'away',
'wile': 'want',
}

# rules according to pu
# word + word
# word + li + word

# lowercase
# remove non-toki pona charachters unless after jan or nimi
# remove duplicate li's
# remove beginning li's

# functions
def tpSentenceVerifier(tpSentences):
    #stringToVerify = tpSentences
    tpStringsToVerify = tpSentences.split('.')
    tokipona = []
    for sentence in tpStringsToVerify:
        tpListToVerify = sentence.split(' ')
        tpListToVerify = propercases(tpListToVerify)
        tpListToVerify = tpCheckIsWord(tpListToVerify)
        tpListToVerify = elaliRemoveDuplicate(tpListToVerify)
        tokipona.append(' '.join(tpListToVerify))
        tokipona.append('.')
    tokipona = ' '.join(tokipona)
    return tokipona

def propercases(tpListToVerify):
    checkList = tpListToVerify[:]
    for index,word in enumerate(tpListToVerify):
        tpListToVerify[index] = word.lower()
        if tpListToVerify[index - 1] == 'jan' or tpListToVerify[index - 1] == 'nimi':
            tpListToVerify[index] = word.capitalize()
    if checkList != tpListToVerify:
        propercases(tpListToVerify)
    return tpListToVerify

def tpCheckIsWord(tpListToVerify):
    checkList = tpListToVerify[:]
    for index,word in enumerate(tpListToVerify):
        if tpdictionary.get(word) == None and tpListToVerify[index - 1] == 'jan' or tpListToVerify[index - 1] == 'nimi':
           continue
        elif tpdictionary.get(word) == None:
            del tpListToVerify[index]
        else:
            continue
    if checkList != tpListToVerify:
        tpCheckIsWord(tpListToVerify)
    #print(' '.join(tpListToVerify))           
    return tpListToVerify
    
def elaliRemoveDuplicate(tpListToVerify):
    checkList = tpListToVerify[:]
    for tpword in ['li','la','e']:
        for index, word in enumerate(tpListToVerify):
            #print(index,len(tpListToVerify))
            if word == tpword and index == 0:
                del tpListToVerify[index]
            elif word == tpword and index < len(tpListToVerify)-1:
                if tpListToVerify[index + 1] == tpword:
                    del tpListToVerify[index + 1]
            elif word == tpword and index+1 == len(tpListToVerify):
                del tpListToVerify[index]
        #print(' '.join(tpListToVerify))
    if checkList != tpListToVerify:
        elaliRemoveDuplicate(tpListToVerify)
    return tpListToVerify


    
def OneWordTranslate():
    tpword = input("\n sona ala ni anu seme? ")
    englishword = tpdictionary.get(tpword,"*nothing in toki pona!*")
    print("\n", tpword, 'means', englishword)
    again = input("\n lookup another, \'y\' or \'n\'? ")
    if again == "y":
        OneWordTranslate()
    else:
        end = input("\n close program")

def SentanceTranslate():
    tpsentenceList = str(input("\n sona ala ni anu seme? "))
    tpSentence = tpsentenceList.split()
    englishsentece = []
    for word in tpSentence:
        tpword = tpdictionary.get(word,"nothing in toki pona!")
        englishsentece.append(tpword)
    print("\n", ' '.join(englishsentece))
    again = input("\n translate another, \'y\' or \'n\'? ")
    if again == "y":
        SentanceTranslate()
    else:
        end = input("\n close program")

def choice():
    WordOrSentence = input("translate sentence \'s\' or lookup word \'w\'? ")
    if WordOrSentence == "w":
        OneWordTranslate()   
    elif WordOrSentence == "s":
        SentanceTranslate()
    else:
        print("seme?")
        choice()
 

# translate toki pona to english!

tpInput = input("What is your toki pona? ")
tp = tpSentenceVerifier(tpInput)
tp = tpSentenceVerifier("mi jo sowli nimi Skylab. soweli nimi Skylab li li pona e")
print(tp)
 
#choice()

#print("\n")
#for tpword, englishword in tpdictionary():
#    print(key, " means ", value)