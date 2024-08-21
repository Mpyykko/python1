import json
import random


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
                    else:
                        oikea_vastaus_kirjain = chr(97 + n.index(oikea_vastaus_idx))
                        print(f'Väärä vastaus! Saavutit {pisteet} pistettä\n')
                        print(f'Oikea vastaus olisi ollut ({oikea_vastaus_kirjain}) {kysymykset[str(x)][oikea_vastaus_idx]}')

                        print('Peli loppui.')
                        return 
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
