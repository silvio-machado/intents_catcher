# -*- encoding: utf-8 -*-
import json
import os.path

from . import intents_classes
from . import phrase_refiner

INTENTS_FILE_PATH = os.path.join(os.path.dirname(__file__), "intents.json")
        
with open(INTENTS_FILE_PATH, "r") as json_content:
    intents = json.load(json_content)
    
intencao = {}

# for chave in intents['compra']:
#     intencao[chave] = comprar

# for chave in intents['venda']:
#     intencao[chave] = vender

for key in intents:
    intent_class = getattr(intents_classes, key)
    intent = intent_class()
    for sub_intent in intents[key]:
        intencao[sub_intent] = intent
        
def catcher(text):
    quest = phrase_refiner.object_refiner(text).split()
    for word in quest:
        if word in intencao:
            objeto = " ".join(quest[quest.index(word)+1:])
            return"a intencao é {} aplicavel em {}".format(
                word,
                objeto)      
