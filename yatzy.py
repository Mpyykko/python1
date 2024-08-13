import random

class YksNoppa:
    def __init__(self):
        self.value = random.randint(1, 6)

    def heitto(self):
        self.value = random.randint(1, 6)
        return self.value

    def __repr__(self):
        return str(self.value)

class KaikkiNopat:
    def __init__(self, nopan_numero=5):
        self.noppa = [YksNoppa() for _ in range(nopan_numero)]

    def roll(self, pidetyt_nopat=[]):
        for i in range(len(self.noppa)):
            if i not in pidetyt_nopat:
                self.noppa[i].heitto()
        return self.noppa

    def values(self):
        return [yks_noppa.value for yks_noppa in self.noppa]

    def __repr__(self):
        return ' '.join(map(str, self.noppa))

class TulosLista:
    tulos_rivi = [
        '1', '2', '3', '4', '5', '6',
        'kolmoset', 'neloset', 'mökki', 'pikkusuora', 'isosuora', 
        'sattuma', 'yatzy', 'pari', '2paria' 
    ]

    def __init__(self):
        self.tulos = {tulos_rivi: None for tulos_rivi in self.tulos_rivi}

    def calculate_score(self, noppa, tulos_rivi):
        values = noppa.values()
        if tulos_rivi == '1':
            return values.count(1)
        elif tulos_rivi == '2':
            return values.count(2) * 2
        elif tulos_rivi == '3':
            return values.count(3) * 3
        elif tulos_rivi == '4':
            return values.count(4) * 4
        elif tulos_rivi == '5':
            return values.count(5) * 5
        elif tulos_rivi == '6':
            return values.count(6) * 6
        elif tulos_rivi == 'kolmoset':
            for i in range(1, 7):
                if values.count(i) >= 3:
                    return sum(values)
            return 0
        elif tulos_rivi == 'neloset':
            for i in range(1, 7):
                if values.count(i) >= 4:
                    return sum(values)
            return 0
        elif tulos_rivi == 'mökki':
            if any(values.count(i) == 3 for i in range(1, 7)) and any(values.count(i) == 2 for i in range(1, 7)):
                return 25
            return 0
        elif tulos_rivi == 'pikkusuora':
            if len(set(values)) >= 4 and any(set(straight).issubset(set(values)) for straight in [range(1, 5), range(2, 6), range(3, 7)]):
                return 30
            return 0
        elif tulos_rivi == 'isosuora':
            if set(values) == set(range(1, 6)) or set(values) == set(range(2, 7)):
                return 40
            return 0
        elif tulos_rivi == 'sattuma':
            return sum(values)
        elif tulos_rivi == 'yatzy':
            if len(set(values)) == 1:
                return 50
            return 0
        elif tulos_rivi == '2paria':
            return sum(values) + 10
        elif tulos_rivi == 'pari':
            for i in range(1, 7):
                if values.count(i) >= 2:
                    return sum(values)
            return 0
        return 0

    def record_score(self, dice, category):
        if self.tulos[category] is None:
            self.tulos[category] = self.calculate_score(dice, category)
        else:
            raise ValueError(f"'{category}' on jo tulos.")

    def total_score(self):
        return sum(score for score in self.tulos.values() if score is not None)

    def __repr__(self):
        return str(self.tulos)

class Pelaaja:
    def __init__(self, nimi):
        self.nimi = nimi
        self.scorecard = TulosLista()

    def take_turn(self):
        dice_set = KaikkiNopat()
        print(f"{self.nimi} heittää")
        print(f"Eka heitto: {dice_set}")
        
        for roll in range(2):
            keep = input("Pidettävät nopat (välilyönnillä erotettuna esim., 0 2 4): ").split()
            keep_indices = [int(i) for i in keep if i.isdigit()]
            dice_set.roll(keep_indices)
            print(f"Heitto {roll + 2}: {dice_set}")
        
        while True:
            category = input("Mihin tulos laitetaan: ").strip().lower()
            if category in self.scorecard.tulos_rivi:
                try:
                    self.scorecard.record_score(dice_set, category)
                    break
                except ValueError as e:
                    print(e)
            else:
                print("Ei tuloslistalla, valitse uudestaan.")
        
        print(f"Tuloslista: {self.scorecard}")

    def total_score(self):
        return self.scorecard.total_score()

    def __repr__(self):
        return f"{self.nimi}: {self.total_score()} pistettä"
    
class Yatzy:
    def __init__(self, players):
        self.players = [Pelaaja(name) for name in players]

    def play(self):
        num_rounds = len(TulosLista.tulos_rivi)  # Adjust number of rounds based on categories
        for round in range(num_rounds):
            print(f"\nKierros: {round + 1}")
            for player in self.players:
                player.take_turn()
        
        self.display_winner()

    def display_winner(self):
        scores = {player.nimi: player.total_score() for player in self.players}
        winner = max(scores, key=scores.get)
        print("\nLopputulokset:")
        for player in self.players:
            print(player)
        print(f"\nVoittaja: {winner}!")

if __name__ == "__main__":
    player_names = input("Anna pelaajanimi (pilkulla erotettuina): ").split(',')
    game = Yatzy([name.strip() for name in player_names])
    game.play()