#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Tämä laskee kuika monta kahden kirjaimen vaihtamista tarvittaisiin järjestämään kirjainlista aakkosjärjestykseen

def solve(kirjainjono):
    pituus = len(kirjainjono)
    jarjestetty = sorted(kirjainjono)
    print(kirjainjono)
    print(jarjestetty)

    # Kuinka paljon alusta yksittäisiä kirjaimia
    A_pituus = 0 
    B_pituus = 0
    C_pituus = 0
    for ii in range(pituus):
        if jarjestetty[ii] == 'A':
            A_pituus += 1
        elif jarjestetty[ii] == 'B':
            B_pituus += 1
        else:
            break
    C_pituus = pituus - A_pituus - B_pituus

    # Lasketaan siirrot:
    # A_vaarin = []
    # B_vaarin = []
    # C_vaarin = []
    siirtoja = 0
    for ii in range(pituus):
        if ii < A_pituus :                                          # A:n paikat
            if kirjainjono[ii] == 'B':
                B_vaarin.append(ii)
            elif kirjainjono [ii] == 'C':
                C_vaarin.append(ii)
        if (ii >= A_pituus) and ii < (A_pituus + B_pituus) :        # B:n paikat
            if kirjainjono[ii] == 'A':
                A_vaarin.append(ii)
            elif kirjainjono[ii] == 'C':
                C_vaarin.append(ii)
        else:                                                       # C:n paikat
            if kirjainjono[ii] == 'A':
                A_vaarin.append(ii)
            elif kirjainjono[ii] == 'B':
                B_vaarin.append(ii)
    print (A_vaarin,B_vaarin,C_vaarin)

    # Siirtojen määrä
    # siirtoja = 0
    # for ii in range(pituus):
    #     if ii < A_pituus and kirjainjono[ii] != 'A':                # A:n paikat
    #         siirtoja += 1
    #         # kokeillaan saadaanko fiksattua samalla B:n ja C:n vääriä paikkoja
    #         if (kirjainjono[ii] == 'B') and (A_vaarin[0] < (A_pituus + B_pituus) ): 
                




if __name__ == "__main__":
    print(solve("CCAABB")) # 4
    #print(solve("CBACBA")) # 3
    #print(solve("AAAA")) # 0