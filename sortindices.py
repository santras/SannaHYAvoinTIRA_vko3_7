#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#import sys
#from time import time
#from random import shuffle

    

def get(tt):
    # TODO

    tuuplislista = []
    indeksilista = []

    for ii in range(len(tt)):
        tuuplislista.append((ii,tt[ii]))
    #print(tuuplislista)
    
    tuuplislista = sorted(tuuplislista, key = lambda numero : numero[1] )
    #print(tuuplislista)
    
    for ii in range(len(tt)):
        indeksilista.append(tuuplislista[ii][0])
    
    return indeksilista
    


if __name__ == "__main__":
    print(get([1,2,4,3])) # [0,1,3,2]
    print(get([4,2,1,3])) # [2,1,3,0]
    print(get([6,2,8,5,3])) # [1,4,3,0,2]