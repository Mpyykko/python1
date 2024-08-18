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
    n = [0, 1, 2, 3]
    m = []
    
    for i in range(5):
        x = random.randint(1, len(helpot_kysymykset))
        random.shuffle(n)
        
        while x in m:
            x = random.randint(1, len(helpot_kysymykset))
        m.append(x)
        print()
        
        vastausvaihtoehdot = n.copy()
        oikea_vastaus_idx = int(helpot_kysymykset[str(x)][-1])
        
        print(f'{helpot_kysymykset[str(x)][4]}')
        
        while True:
            try:
                for idx, vaihtoehto in enumerate(vastausvaihtoehdot):
                    print(f'    ({chr(97 + idx)}) {helpot_kysymykset[str(x)][vaihtoehto]}')
                if oljenkorsi1:
                    print('(1) Oljenkorsi 1: Poista 1 väärä vastaus')
                if oljenkorsi2:
                    print('(2) Oljenkorsi 2: Poista 2 väärää vastausta')
                
                valinta = input('Vastauksesi: ').strip().lower()
                
                if valinta in ['a', 'b', 'c', 'd']:
                    if n[['a', 'b', 'c', 'd'].index(valinta)] == oikea_vastaus_idx:
                        pisteet += 1
                    else:
                        print(f'Väärä vastaus! Saavutit {pisteet} pistettä\n')
                        print('Peli loppui.')
                        return 
                    break
                
                elif valinta == '1' and oljenkorsi1:
                    oljenkorsi1 = False
                    vaarat_vaihtoehdot = [v for v in vastausvaihtoehdot if v != oikea_vastaus_idx]
                    if vaarat_vaihtoehdot:
                        poistettava = random.choice(vaarat_vaihtoehdot)
                        vastausvaihtoehdot.remove(poistettava)
                  
            
                elif valinta == '2' and oljenkorsi2:
                    oljenkorsi2 = False
                    vaarat_vaihtoehdot = [v for v in vastausvaihtoehdot if v != oikea_vastaus_idx]
                    if len(vaarat_vaihtoehdot) >= 2:
                        poistettavat = random.sample(vaarat_vaihtoehdot, 2)
                        for poistettava in poistettavat:
                            vastausvaihtoehdot.remove(poistettava)
                
                
                else:
                    print('Virheellinen valinta tai oljenkorsi on jo käytetty\n')
            
            except ValueError:
                print('Virheellinen valinta\n')

if __name__ == '__main__':
    visa_valikko()
