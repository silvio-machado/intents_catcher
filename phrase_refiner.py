# -*- encoding:utf-8 -*-
_TO_REMOVE = ['um','uma', 'outra', 'outro', 'algumas','alguns',
              'de', 'da', 'do', 'meu', 'minha', 'nossa',]
_BLANK = ''

def object_refiner(phrase):
    for word in _TO_REMOVE:
        if word in phrase:
            phrase = phrase.replace(word+' ', _BLANK)
    return phrase 
