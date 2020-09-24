#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#import sys
from time import time


def jarjesta(nn):
    alku = time()

    loppu = time()
    return loppu-alku


if __name__ == "__main__":
    print(jarjesta(10)) # 0
    #print(jarjesta(1000)) # 0
    #print(jarjesta(10000)) # 2
    #print(jarjesta(100000)) # 3