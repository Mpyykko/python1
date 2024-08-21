from datetime import datetime
from tietovisa import visa_valikko
from yatzy import Yatzy



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

def pelivalikko():
    while True:
        try:
            print('Valitse peli: \n(1) Lottoarvonta\n(2) Yatzy\n(3) Tietovisa\n(4) Lopetus')
            valinta = int(input('Valinta: '))
            if valinta == 1:
                from lotto import lottoarvonta
                lottoarvonta()
                break
            elif valinta == 2:
                pelaajien_nimet = input("Anna pelaajanimi/-nimet (pilkulla erotettuina): ").split(',')
                peli = Yatzy([name.strip() for name in pelaajien_nimet])
                peli.pelaa()
                print()
                break
            elif valinta == 3:
                visa_valikko()
                print()
                break
            elif valinta == 4:
                heippa()
                break
            else:
                print('Tuntematon valinta')
                print()

            
            
        except ValueError:
            print('Anna kokonaisluku')
            print()
    


