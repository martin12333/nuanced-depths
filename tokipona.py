# Will be migrated to a module shortly

# the toki pona dictionary as simple as I could make it!
tpdictionary = {
'a': 'ah!',
'akesi': 'reptile',
'ala': 'none',
'alasa': 'hunt or gather',
'ale': 'all',
'anpa': 'under',
'ante': 'different',
'anu': 'or',
'awen': 'wait',
'e': 'the (to introduce the direct object)',
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
'kala': 'sea creature',
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
'kon': 'wind or smell',
'kule': 'colour',
'kulupu': 'club',
'kute': 'listen',
'la': '*goes between phrase of context and sentence*',
'lape': 'sleep',
'laso': 'blue-green',
'lawa': 'head',
'len': 'clothes',
'lete': 'cold',
'li': '*goes between subject and verb*',
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
'mi': 'i',
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
'net': 'the Internet',
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
'waso': 'bird',
'wawa': 'power',
'weka': 'away',
'wile': 'want',
}

def ante_toki(sentence):
  words = sentence.lower().split()
  translated_words = []
  for word in words:
    translated_words.append(tpdictionary.get(word, word))
  out = ' '.join(translated_words)
  return out
  
def translator(sentence):
  words = sentence.lower().split()
  dict_inverse = {v:k for k,v in tpdictionary.items()}
  translated_words = []
  for word in words:
    translated_words.append(dict_inverse.get(word, word))
  out = ' '.join(translated_words)
  return out
  
mode = input('Input language, \'t\' for tokipona, \'e\' for English:\n')
print()
sentence_to_translate = input('Type a sentence to translate:\n')

if mode == 't':
  print(ante_toki(sentence_to_translate))
elif mode == 'e':
  print(translator(sentence_to_translate))
else:
  print('Mode not recognised :(')
  exit(1)
  
'''

# Simple query of dictionary, good for one word at a time

tpword = input("sona ala ni anu seme? ")
englishword = tpdictionary.get(tpword,"nothing in toki pona!")
print(tpword, 'means', englishword)
#print("Not a toki pona word!")

'''