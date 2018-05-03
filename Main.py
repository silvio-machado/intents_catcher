# -*- encoding: utf-8 -*-
import json

class compra:
    def comprar(self):
        print("Estou comprando.")

class venda():
    def vender(self):
        print("Estou vendendo.")


        
with open("intents.json", "r") as json_content:
    intents = json.load(json_content)
    
intencao = {}
comprar = compra()
vender = venda()

for chave in intents['compra']:
    intencao[chave] = comprar

for chave in intents['venda']:
    intencao[chave] = vender
    
while True:
    quest = input("$: " ).split()
    for word in quest:
        if word in intencao:
            objeto = " ".join(quest[quest.index(word)+1:])
            print("a intencao eh {} e o desejo eh {}".format(word, objeto))
            break            
