#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from time import time
from collections import deque

def listat(nn):

    # EKA TESTI
    # normilistat
    n1_alku = time()
    normi_lista = []

    for ii in range(1,nn+1):
        normi_lista.append(ii)
    #print(normi_lista)

    for ii in range(nn,0,-1):
        normi_lista.pop()
        #print(ii,normi_lista)
    #print(normi_lista)

    n1_loppu = time()


    # EKA TESTI
    # solmulistat
    s1_alku = time()
    solmu_lista = deque()

    for ii in range(1,nn+1):
        solmu_lista.append(ii)
    

    for ii in range(nn,0,-1):
        solmu_lista.pop()

    s1_loppu = time()

    #TOKATESTI
    # normilistat
    n2_alku = time()
    normi_lista = []

    for ii in range(1,nn+1):
        normi_lista.append(ii)
    #print(normi_lista)

    for ii in range(0,nn):
        normi_lista.pop(0)
        #print(ii,normi_lista)
    #print(normi_lista)
    n2_loppu = time()


    # TOKA TESTI
    # solmulistat

    s2_alku = time()
    solmu_lista = deque()

    for ii in range(1,nn+1):
        solmu_lista.append(ii)
    

    for ii in range(0,nn):
        solmu_lista.popleft()

    s2_loppu = time()



    return n1_loppu - n1_alku, s1_loppu - s1_alku, n2_loppu - n2_alku, s2_loppu - s2_alku


if __name__ == "__main__":
    #print(listat(10))
    print(listat(100000))