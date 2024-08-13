from random import sample
from datetime import datetime
import time

def lottoarvonta():
    
    print('Pelataan siis lottoa!')
    print()
    numerot = []
    osuneet = []
    arvotut_numerot = list(range(1,41))
    rivi = sample(arvotut_numerot, 7)
    osumat = 0
    luku =1
    time.sleep(1.4)
    print('Arvotaan 7 numeroa väliltä 1-40')
    #print(rivi)
    print()

    
    
    while luku <= 7:
        try:
            numero = int(input(f'Anna {luku}.numero: '))
            if numero in numerot:
                 print('Ei voi antaa kahta samaa numeroa')
                 continue
        
            if numero <1:
                print('Liian pieni numero!')
                continue
            if numero >40:
                print('Liian suuri numero!')
                continue
            numerot.append(numero)
            luku +=1
      

        except ValueError:
                print('Numeron täytyy olla luku')
        
    print()

    for i in numerot:
            if i in rivi:
                osumat +=1

    print (f'Antamasi numerot: {'  '.join(f'{i:2}' for i in numerot)} ')

   
    print('Arvotaan rivi:   ', end='', flush=True)
    for i in rivi:
        print(f' {i:2} ', end='', flush=True)
        time.sleep(0.9)
                
    
    for i in numerot:
         if i in rivi:
              osunut_numero = i
              osuneet.append(i)

    if osumat == 1:
         print()
         print (f'Sait yhden oikein! Osunut numero: {osunut_numero}')
    elif osumat >0:
         print()
         print (f'Sait {osumat} oikein! Osuneet numerot: {'  '.join(str(i) for i in osuneet)}')
    else:
         print()
         print('Ei yhtään osumaa')
    print()
    while True:
        try:
            time.sleep(1.5)
            print ('Mitä seuraavaksi? \n(1) Pelaa uudelleen\n(2) Aloitusvalikko\n(3) Lopetus')
            valinta =int(input('Valinta: '))
            if valinta == 1:
                lottoarvonta()
                break
            elif valinta == 2:
                aloitus_valikko()
                break
            elif valinta == 3:
                heippa()
                break      
            else:
                print('Tuntematon valinta')
                print()
                continue
        
        except ValueError:
            print('Anna kokonaisluku')
            print()
        
    

def heippa():
    nyt = datetime.now()
    tunnit = nyt.hour
    aamu_alku = 5
    aamu_loppu = 10
    paiva_alku = 10
    paiva_loppu = 17
    ilta_alku = 17
    ilta_loppu = 23

    if aamu_alku <= tunnit <= aamu_loppu:
        print('Mukavaa aamun jatkoa!')
    elif paiva_alku <= tunnit <= paiva_loppu:
        print('Kivaa päivän jatkoa!')
    elif ilta_alku <= tunnit <= ilta_loppu:
        print('Hyvää illan jatkoa!')
    else:
        print('Hyvää yötä!')


def aloitus_valikko():
    print()
    print()
    print()
    print('Tervetuloa pelaamaan!')
    print()
    while True:
        try:
            print ('Valitse peli: \n(1) Lottoarvonta\n(2) Joku muu\n(3) Lopetus')
            valinta =int(input('Valinta: '))
            if valinta == 1:
                lottoarvonta()
                break
            elif valinta == 2:
                print('Peli ei vielä saatavilla')
                print()
            
            elif valinta == 3:
                heippa()
                break

        
        except ValueError:
            print('Anna kokonaisluku')
            print()

####################################   Pääohjelma alkaa   ####################################

aloitus_valikko()
#print('\033[91mTämä teksti on punaista\033[0m')
#print('\033[91mPunainen\033[0m \033[32mVihreä\033[0m')


