from random import sample
import time
from utils import pelivalikko

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
    pelivalikko()
