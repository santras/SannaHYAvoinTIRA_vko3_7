#!/usr/bin/env python
# -*- coding: utf-8 -*- 


def changes(tt):

    #print(tt)
    maxit=[0]*(len(tt))

    # Tehdään lista jossa maximi vasemmalta katsottuna
    maxit[0] = tt[0]
    for ii in range(1,len(tt)):
        maxit[ii] = max(maxit[ii-1],tt[ii])
    #print(maxit)
    
    # Lasketaan siirtojen määrä
    siirrot = 0
    for ii in range(len(tt)):
        siirrot += (maxit[ii]-tt[ii]) 
    return siirrot


if __name__ == "__main__":
    print(changes([3,2,5,1,7])) # 5
    print(changes([1,2,3,4,5])) # 0
    print(changes([3,3,1,4,2])) # 4