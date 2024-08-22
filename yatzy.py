import random

class Noppa:
    def __init__(self):
        self.arvo = random.randint(1, 6)

    def heitä(self):
        self.arvo = random.randint(1, 6)
        return self.arvo

    def __repr__(self):
        return str(self.arvo)

class Nopat:
    def __init__(self, nopan_numero=5):
        self.nopat = [Noppa() for _ in range(nopan_numero)]

    def heitä(self, pidetyt_numerot=[]):
        for i in range(len(self.nopat)):
            if i not in pidetyt_numerot:
                self.nopat[i].heitä()
        return self.nopat

    def arvot(self):
        return [noppa.arvo for noppa in self.nopat]

    def __repr__(self):
        return ' '.join(map(str, self.nopat))

class Tuloskortti:
    tuloskortti = [
        '1', '2', '3', '4', '5', '6',
        'kolmoset', 'neloset', 'mökki', 'pikkusuora', 'isosuora', 
        'sattuma', 'yatzy', 'pari', '2paria' 
    ]

    def __init__(self):
        self.pisteet = {rivi: None for rivi in self.tuloskortti}

    def laske_pisteet(self, nopat, rivi):
        arvot = nopat.arvot()
        if rivi == '1':
            return arvot.count(1)
        elif rivi == '2':
            return arvot.count(2) * 2
        elif rivi == '3':
            return arvot.count(3) * 3
        elif rivi == '4':
            return arvot.count(4) * 4
        elif rivi == '5':
            return arvot.count(5) * 5
        elif rivi == '6':
            return arvot.count(6) * 6
        elif rivi == 'kolmoset':
            kolmoset = []
            for i in range(1, 7):
                if arvot.count(i) >= 3:
                    kolmoset.append(i)
                    return sum(kolmoset * 3)
            return 0
        elif rivi == 'neloset':
            neloset = []
            for i in range(1, 7):
                if arvot.count(i) >= 4:
                    neloset.append(i)
                    return sum(neloset * 4)
            return 0
        elif rivi == 'mökki':
            if any(arvot.count(i) == 3 for i in range(1, 7)) and any(arvot.count(i) == 2 for i in range(1, 7)):
                return 25
            return 0
        elif rivi == 'pikkusuora':
            if len(set(arvot)) >= 4 and any(set(suora).issubset(set(arvot)) for suora in [range(1, 5), range(2, 6), range(3, 7)]):
                return 30
            return 0
        elif rivi == 'isosuora':
            if set(arvot) == set(range(1, 6)) or set(arvot) == set(range(2, 7)):
                return 40
            return 0
        elif rivi == 'sattuma':
            return sum(arvot)
        elif rivi == 'yatzy':
            if len(set(arvot)) == 1:
                return 50
            return 0
        elif rivi == '2paria':
            parit = []
            for i in range(1, 7):
                if arvot.count(i) >= 2:
                    parit.append(i)
            if len(parit) >= 2:
                return sum(pari * 2 for pari in parit[:2])
            return 0
        elif rivi == 'pari':
            pari = []
            for i in range(1, 7):
                if arvot.count(i) >= 2:
                    pari.append(i)
            return (max(pari) * 2)
        return 0

    def tallenna_tulos(self, nopat, kategoria):
        if self.pisteet[kategoria] is None:
            self.pisteet[kategoria] = self.laske_pisteet(nopat, kategoria)
        else:
            raise ValueError(f"'{kategoria}' on jo tallennettu.")

    def kokonaispisteet(self):
        return sum(piste for piste in self.pisteet.values() if piste is not None)

    def __repr__(self):
        return str(self.pisteet)
    
    def näytä_tuloskortti(self):
        print("Tuloskortti:")
        for kategoria, piste in self.pisteet.items():
            status = piste if piste is not None else "-"
            print(f"{kategoria}: {status}")
        print()

class Pelaaja:
    def __init__(self, nimi):
        self.nimi = nimi
        self.tuloskortti = Tuloskortti()

    def heittovuoro(self):
        nopat = Nopat()
        self.tuloskortti.näytä_tuloskortti()
        print(f"{self.nimi} heittää")
        print(f"Eka heitto: {nopat}")
        
        for heitto in range(2):
            pidettävät = input("Pidettävät nopat (välilyönnillä erotettuna, esim. 1 2 5): ").split()
            pidetyt_numerot = [int(i)-1 for i in pidettävät if i.isdigit()]
            nopat.heitä(pidetyt_numerot)
            print(f"Heitto {heitto + 2}: {nopat}")
        
        while True:
            kategoria = input("Mihin tulos laitetaan: ").strip().lower()
            if kategoria in self.tuloskortti.tuloskortti:
                try:
                    self.tuloskortti.tallenna_tulos(nopat, kategoria)
                    break
                except ValueError as e:
                    print(e)
            else:
                print("Ei tuloslistalla, valitse uudestaan.")
        
        #print(f"Tuloskortti: {self.tuloskortti}")

    def kokonaispisteet(self):
        return self.tuloskortti.kokonaispisteet()

    def __repr__(self):
        return f"{self.nimi}: {self.kokonaispisteet()} pistettä"
    
class Yatzy:
    def __init__(self, pelaajat):
        self.pelaajat = [Pelaaja(nimi) for nimi in pelaajat]

    def pelaa(self):
        kierrokset = len(Tuloskortti.tuloskortti)
        for kierros in range(kierrokset):
            print(f"\nKierros: {kierros + 1}")
            for pelaaja in self.pelaajat:
                pelaaja.heittovuoro()
        
        self.näytä_voittaja()

    def näytä_voittaja(self):
        pisteet = {pelaaja.nimi: pelaaja.kokonaispisteet() for pelaaja in self.pelaajat}
        voittaja = max(pisteet, key=pisteet.get)
        print("\nLopputulokset:")
        for pelaaja in self.pelaajat:
            print(pelaaja)
        print(f"\nVoittaja: {voittaja}!")

if __name__ == "__main__":
    pelaajien_nimet = input("Anna pelaajanimi/-nimet (pilkulla erotettuina): ").split(',')
    peli = Yatzy([nimi.strip() for nimi in pelaajien_nimet])
    peli.pelaa()
