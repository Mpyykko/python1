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
