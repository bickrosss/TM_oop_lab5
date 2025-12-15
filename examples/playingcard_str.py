from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str

    def __str__(self):
        return f'{self.suit}{self.rank}'

if __name__ == "__main__":
    ace_of_spades = PlayingCard('A', '♠')
    print(ace_of_spades)