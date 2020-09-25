#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def count(lista,maxpaino):
    lista.sort()
    #print(lista)
    #print('max paino',maxpaino)
    pienet_kaytetty = 0     # pienet postitettu tähän indeksiin asti
    pienet_mukana = 0       # pieniä postitettu isojen pakettien mukana



    for ii in range(len(lista)-1,-1,-1):
        #print(lista[ii], lista[pienet_kaytetty])
        if pienet_kaytetty< ii:
            if lista[ii] + lista[pienet_kaytetty] <= maxpaino:
                pienet_mukana += 1
                pienet_kaytetty += 1
        else:
            return len(lista)-pienet_kaytetty

    return len(lista)-pienet_kaytetty
    
    #print(len(lista),pienet_mukana)

    

if __name__ == "__main__":
    print(count([1,2,3,4],10)) # 2
    print(count([4,4,4,4],5)) # 4
    print(count([7,2,3,9],10)) # 3
    print(count([4,2,1,5,3],6)) # 3