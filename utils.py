from datetime import datetime
import os
import sys,time


clear = lambda: os.system('cls')
clear()

def heippa():
    nyt = datetime.now()
    tunnit = nyt.hour
    aamu_alku = 5
    aamu_loppu = 10
    paiva_alku = 10
    paiva_loppu = 17
    ilta_alku = 17
    ilta_loppu = 23

    print()
    if aamu_alku <= tunnit <= aamu_loppu:
        print('Mukavaa aamun jatkoa!')
    elif paiva_alku <= tunnit <= paiva_loppu:
        print('Kivaa päivän jatkoa!')
    elif ilta_alku <= tunnit <= ilta_loppu:
        print('Hyvää illan jatkoa!')
    else:
        print('Hyvää yötä!')
    print()

def pelivalikko():
    from tietovisa import visa_valikko
    from yatzy import Yatzy

    print()
    while True:
        try:
            print('Valitse peli: \n(1) Lottoarvonta\n(2) Yatzy\n(3) Tietovisa\n(4) Lopetus')
            valinta = int(input('Valinta: '))
            if valinta == 1:
                from lotto import lottoarvonta
                clear()
                lottoarvonta()
                break
            elif valinta == 2:
                clear()
                pelaajien_nimet = input("Anna pelaajanimi/-nimet (pilkulla erotettuina): ").split(',')
                peli = Yatzy([nimi.strip() for nimi in pelaajien_nimet])
                peli.pelaa()
                print()
                break
            elif valinta == 3:
                clear()
                visa_valikko()
                print()
                break
            elif valinta == 4:
                clear()
                heippa()
                break
            else:
                print('Tuntematon valinta')
                print()

            
            
        except ValueError:
            print('Anna kokonaisluku')
            print()

    
def progress_bar(iteration, total, length=50):
    percent = ('{0:.1f}').format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent}% Complete')
    sys.stdout.flush()

total = 100
for i in range(total + 1):
    time.sleep(0.03)
    progress_bar(i, total)


    

    


