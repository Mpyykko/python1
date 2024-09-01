import json
import random
from utils import pelivalikko

import time

def lataa_kysymykset(tiedosto):
    with open(tiedosto, 'r', encoding='utf-8') as f:
        kysymykset = json.load(f)
    return kysymykset
def visa_valikko():
    oljenkorsi1 = True
    oljenkorsi2 = True
    pisteet = 0
    helpot_kysymykset = lataa_kysymykset('kysymykset-helpot.json')
    vaikeat_kysymykset = lataa_kysymykset('kysymykset-vaikeat.json')
    n = [0, 1, 2, 3]
    m = []
    def kayta_oljenkorsi(valinta):
        vaarat_vaihtoehdot = [v for v in vastausvaihtoehdot if v != oikea_vastaus_idx]
        poistettava = random.sample(vaarat_vaihtoehdot, int(valinta))
        if valinta == '1':           
            kysymykset[str(x)][poistettava[0]] = ''                      
        elif valinta == '2':
            for p in poistettava:
                kysymykset[str(x)][p] = ''
    
    for i in range(10):
        if i == 5:
            m = []
        if i<=4:
            kysymykset = helpot_kysymykset
        elif i >= 5:
            kysymykset = vaikeat_kysymykset
        x = random.randint(1, len(kysymykset))
        random.shuffle(n)
        
        while x in m:
            x = random.randint(1, len(kysymykset))
        m.append(x)
        print()
        
        vastausvaihtoehdot = n.copy()
        oikea_vastaus_idx = int(kysymykset[str(x)][-1])

        time.sleep(1)
        
        print(f'{kysymykset[str(x)][4]}')                        
        
        while True:
            try:
                for idx, vaihtoehto in enumerate(vastausvaihtoehdot):
                    print(f'    ({chr(97 + idx)}) {kysymykset[str(x)][vaihtoehto]}')
                if oljenkorsi1:
                    print('(1) Oljenkorsi 1: Poista 1 väärä vastaus')
                if oljenkorsi2:
                    print('(2) Oljenkorsi 2: Poista 2 väärää vastausta')
                
                valinta = input('Vastauksesi: ').strip().lower()
                
                
                if valinta in ['a', 'b', 'c', 'd']:
                    
                    if n[['a', 'b', 'c', 'd'].index(valinta)] == oikea_vastaus_idx:
                        pisteet += 1
                        print()
                        print('\033[1;32mOikein!\033[0m')
                        print(f'Pisteet: {pisteet}')
                        if pisteet == 10:
                            print('\033[1;34mYou made it, Pal!\033[0m')
                            time.sleep(2)
                            pelivalikko()

                    else:
                        print(f'\033[1;31mVäärä vastaus!\033[0m Saavutit {pisteet} pistettä\n')
                        print('Peli loppui.')
                        time.sleep(2)
                        pelivalikko()
                    break
                
                elif valinta == '1' and oljenkorsi1:
                    oljenkorsi1 = False
                    kayta_oljenkorsi(valinta)
                elif valinta == '2' and oljenkorsi2:
                    oljenkorsi2 = False
                    kayta_oljenkorsi(valinta)
                
                else:
                    print('Virheellinen valinta tai oljenkorsi on jo käytetty\n')
            
            except ValueError:
                print('Virheellinen valinta\n')

            
            




if __name__ == '__main__':
    visa_valikko()
