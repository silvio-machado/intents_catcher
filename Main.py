# -*- encoding: utf-8 -*-
import json

import intents_classes
import phrase_refiner

        
with open("intents.json", "r") as json_content:
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
    
while True:
    quest = phrase_refiner.object_refiner(input("$: " )).split()
    for word in quest:
        if word in intencao:
            objeto = " ".join(quest[quest.index(word)+1:])
            print("a intencao é {} aplicavel em {}".format(
                word,
                objeto)
            )
            break            
