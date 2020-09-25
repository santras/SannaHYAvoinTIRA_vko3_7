#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def solve(ss):
    ll=len(ss)
    jarjestetty = sorted(ss)
    #print(ss)
    #print(jarjestetty)

    # Kuinka monta nollaa
    nollia = 0
    for ii in range(ll):
        if jarjestetty[ii] != '0':
            break
        else:
            nollia +=1
    #print('nollia',nollia)

    # ykkosia
    #ykkoset = ll-nollia

    # väärässä paikassa olevat 1:set
    vaarin_nollapuoli = []
    for ii in range(nollia):
        if ss[ii] == '1':
            vaarin_nollapuoli.append(ii)

    # Jos ei tarvi mitään muutoksia
    if len(vaarin_nollapuoli) == 0:
        return 0
    
    # vaarassa paikassa olevat 0:t
    vaarin_ykkospuoli = []
    for ii in range(ll-1,nollia-1,-1):
        if ss[ii] == '0':
            vaarin_ykkospuoli.append(ii)
    #print(vaarin_nollapuoli,vaarin_ykkospuoli)
    siirtoja = 0
    for ii in range(len(vaarin_ykkospuoli)):
        siirtoja += vaarin_ykkospuoli[ii] - (nollia - 1) # siirtoja ykkospuolella
        #print('siirtoja ykköset', vaarin_ykkospuoli[ii] - (nollia - 1))
        #print ('siirtoja nollat',(nollia-1)- vaarin_nollapuoli[ii])
        #print('nollia-1',(nollia),)
        siirtoja += (nollia-1)- vaarin_nollapuoli[ii] 

    #print(siirtoja)
    return siirtoja
        


if __name__ == "__main__":
    print(solve("000100")) # 2
    print(solve("111000")) # 9
    print(solve("101010")) # 6