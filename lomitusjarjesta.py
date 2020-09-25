#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#import sys
from time import time
from random import shuffle


def jarjesta(aa,bb):
    #print(lista)
    #print(apu)

    # Paluu, jos ei enää järjestettävää.
    if aa == bb:    
        return
    
    # Puolittaminen ja rekursiivinen kutsu
    kk = (aa+bb)//2    
    #print(aa,bb,kk) 
    jarjesta(aa,kk)
    jarjesta(kk+1,bb)
    #print('lomitettavat',aa,kk,kk+1,bb)
    lomita(aa,kk,kk+1,bb)
    

def lomita(a1,b1,a2,b2):
    aa = a1
    bb = b2
    for ii in range(aa,bb+1):
        #print(ii)
        if a2 > b2 or (a1 <= b1 and lista[a1] <= lista[a2]):            # jos a2> b2 jälkimmäinen jono loppu    tai jos ekajonossa on jäljellä ja ekajonon alkio pienempi
            apu[ii] = lista[a1]
            a1 += 1
        else:
            apu[ii] = lista[a2]
            a2 += 1

    #print('apu',apu)
    for ii in range(aa,bb+1):
        lista[ii] = apu [ii]

def lomitusjarjesta(nn):
    alku = time()

    # Tehdään lista joka ei ole järjestyksessä ja apumuuttuja joka yhtä pitkä kuin lista
    global lista, apu
    lista = list(range(1,nn+1))
    apu = [0]*nn
    shuffle(lista)
    #lista = [2, 3, 5, 1, 4, 8, 7, 6]
    #print(lista)
    #print(apu)
    
    # Listan järjestys
    jarjesta(0,nn-1)
    #print(lista)
    loppu = time()
    return loppu-alku


if __name__ == "__main__":
    #print(lomitusjarjesta(8)) 
    print(lomitusjarjesta(1000)) 
    print(lomitusjarjesta(10000)) 
    print(lomitusjarjesta(100000)) 