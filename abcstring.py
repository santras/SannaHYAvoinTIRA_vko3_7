#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Tämä laskee kuika monta kahden kirjaimen vaihtamista tarvittaisiin järjestämään kirjainlista aakkosjärjestykseen

def solve(kirjainjono):
    pituus = len(kirjainjono)
    jarjestetty = sorted(kirjainjono)

    # Kuinka paljon alusta yksittäisiä kirjaimia
    A_pituus = 0 
    B_pituus = 0

    for ii in range(pituus):
        if jarjestetty[ii] == 'A':
            A_pituus += 1
        elif jarjestetty[ii] == 'B':
            B_pituus += 1
        else:
            break

   # Katsotaan erikseen A,B:n paikat ja pistetään ideksit muistiin missä kirjaimia väärällä paikalla
   # C:tä ei tarvitse erikseen katsoa, koska vaihdetaan aina päikseen niin C korjaantuu kun A ja B korjattu
    A_vaarin = []   # Lista A kirjaimen idekseistä jotka ovat A-alueen ulkopuolella
    B_vaarin = []   # Lista B kirjaimen idekseistä jotka ovat A-alueen ulkopuolella

    for ii in range(pituus):
        if ii < A_pituus :                                          # A:n paikat
            if kirjainjono[ii] == 'B':
                B_vaarin.append(ii)
        if (ii >= A_pituus) and ii < (A_pituus + B_pituus) :        # B:n paikat
            if kirjainjono[ii] == 'A':
                A_vaarin.append(ii)
        elif ii >= (A_pituus + B_pituus):                           # C:n paikat
            if kirjainjono[ii] == 'A':
                A_vaarin.append(ii)
            elif kirjainjono[ii] == 'B':
                B_vaarin.append(ii)
   
    #Tarvittava siirtojen määrä kun vaihdetaan pois väärät kirjaimet A:n paikoilta
    siirtoja = 0
    A_ind_alkupaa = 0   # Indeksi virheellisesti oleville A-kirjaimille alkupäästä
    B_fiksattuja = 0
    for ii in range(A_pituus):
        if kirjainjono[ii] != 'A':                
            siirtoja += 1
            # kokeillaan saadaanko fiksattua samalla B:n  vääriä paikkoja
            if (kirjainjono[ii] == 'B') and ( A_vaarin[A_ind_alkupaa] < (A_pituus + B_pituus) ):             # C:t vaihdettaisiin mielummin loppupään kirjaimien kanssa
                B_fiksattuja += 1
                A_ind_alkupaa += 1
            elif (kirjainjono[ii] == 'B'):
                A_ind_alkupaa += 1
    
    # Lisätään siirtoihin virheellisesti sijoitetut B:t lukuunottamatta jo A:n siiroilla fiksattuja
    siirtoja += len(B_vaarin) - B_fiksattuja                # C:t korjaantuvat samalla
    return siirtoja






if __name__ == "__main__":
    print(solve("CCAABB")) # 4
    print(solve("CBACBA")) # 3
    print(solve("AAAA")) # 0
    print(solve("ABBBAABCA")) # 4