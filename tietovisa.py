def visa_valikko():
    oljenkorsi1 = 1
    oljenkorsi2 = 1
    print()
    while True:
        try:
            print('Tähän tulee kysymys?\n    (a) Vastaus1\n    (b) Vastaus2\n    (c) Vastaus3 \n    (d) Vastaus4')
            print()
            if oljenkorsi1 >0:
                print('(1) Oljenkorsi 1: Poista 1 väärä vastaus')
                
            if oljenkorsi2 >0:
                print('(2) Oljenkorsi 2: Poista 2 väärää vastausta')
               
            valinta = input('Vastauksesi: ')
            if valinta == 'a':
                print('Valitsit vaihtoehdon a\n')
                break
            elif valinta == 'b':
                print('Valitsit vaihtoehdon b\n')
                break
            elif valinta == 'c':
                print('Valitsit vaihtoehdon c\n')
                break
            elif valinta == 'd':
                print('Valitsit vaihtoehdon d\n')
                break
            elif valinta == '1':
              
                oljenkorsi1 -=1
            elif valinta == '2':
               
                oljenkorsi2 -=1
            
            else:
                print('Virheellinen valinta\n')
        except ValueError:
            print('Virheellinen valinta\n')



if __name__ == '__main__':
    visa_valikko()

'''
import random

n = [0,1,2,3]
m = []
helpot_kysymykset = {
    1:['Helsinki', 'Halsinki', 'Hulsinki', 'Joku muu', 'Suomen pääkaupunki on?'],
    2:['Tapio Rautavaara', 'Reino Helismaa', 'Georg Otz', 'Kirka', 'Kuka oli tunnettu laulava keihäänheittäjä?'],
    3:['Soisalo', 'Heisalo', 'Koisalo', 'Seisalo', 'Mikä suomalainen näyttelijä-ohjaaja Martti on sukuaan?'],
    4:['3,14', '3,41', '4,13', '1,34', 'Piin likiarvo on?'],
    5:['Simeoni', 'Eero', 'Aapo', 'Lauri', 'Kuka oli kolmanneksi vanhin Jukolan veljeksistä?']
}


def visa_valikko():
    x = random.randint(1, len(helpot_kysymykset))
    for i in range(5):
        random.shuffle(n)
        while x in m:
            x = random.randint(1, len(helpot_kysymykset))
        m.append(x)
        oljenkorsi1 = 1
        oljenkorsi2 = 1
        print()
        while True:
            try:
                print(f'{helpot_kysymykset[x][4]}\n    (a) {helpot_kysymykset[x][n[0]]}\n    (b) {helpot_kysymykset[x][n[1]]}\n    (c) {helpot_kysymykset[x][n[2]]} \n    (d) {helpot_kysymykset[x][n[3]]}')
                print(n, m)
                if oljenkorsi1 >0:
                    print('(1) Oljenkorsi 1: Poista 1 väärä vastaus')
                    
                if oljenkorsi2 >0:
                    
                    print('(2) Oljenkorsi 2: Poista 2 väärää vastausta')
                
                valinta = input('Vastauksesi: ')
                if valinta == 'a':
                    print('Valitsit vaihtoehdon a\n')
                    break
                elif valinta == 'b':
                    print('Valitsit vaihtoehdon b\n')
                    break
                elif valinta == 'c':
                    print('Valitsit vaihtoehdon c\n')
                    break
                elif valinta == 'd':
                    print('Valitsit vaihtoehdon d\n')
                    break
                elif valinta == '1':
                
                    oljenkorsi1 -=1
                elif valinta == '2':
                
                    oljenkorsi2 -=1
                
                else:
                    print('Virheellinen valinta\n')
            except ValueError:
                print('Virheellinen valinta\n')            

if __name__ == '__main__':
    visa_valikko()
'''
