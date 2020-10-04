#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from time import time

# Tämän tehtävän annon tarkoitus on koodata itse ns. linkitetty lista. 

class LinkkiLista:
    def _init_ (self):
        self.stack = []
    
    def lisaa(self, alkio):
        self.stack.append(alkio)
    
    def poista(self):
        self.stack = self.stack[1:]
    
def linkitetty_lista():
    oma = LinkkiLista()
    oma.lisaa(3)
    oma.lisaa(2)
    oma.lisaa(5)
    oma.lisaa(5)
    oma.lisaa(3)
    print(oma)
    oma.poista
    print(oma)



if __name__ == "__main__":

    print(linkitetty_lista())
    #print(listat(100000))