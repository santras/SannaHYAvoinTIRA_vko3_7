#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#import sys
#from time import time
#from random import shuffle

    

def count(tt):
    # TODO
    tt.sort()
    #print(tt)
    valit = []
    valin_alku = 0  # Vuorossa olevan välin alkupä

    for ii in range(len(tt)-1):
        if (tt[ii+1]-tt[ii]) > 1 :        # jos seuraava alkio ei ole seuraava luku järjestyksessä
            valit.append([valin_alku,ii])
            valin_alku = ii+1

    # lisätään viimeinen väli
    valit.append([valin_alku,len(tt)])
    return (len(valit))        


if __name__ == "__main__":
    print(count([4,1,5,3])) # 2
    print(count([4,2,1,3])) # 1
    print(count([5,2,7,6,3,9])) # 3