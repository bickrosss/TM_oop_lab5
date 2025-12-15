from dataclasses import dataclass, field

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♦ ♥ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'

if __name__ == "__main__":
    queen_of_hearts = PlayingCard('Q', '♥')--
    ace_of_spades = PlayingCard('A', '♠')
    
    print(f"queen_of_hearts = {queen_of_hearts}")
    print(f"ace_of_spades = {ace_of_spades}")
    print(f"ace_of_spades > queen_of_hearts: {ace_of_spades > queen_of_hearts}")
    print(f"sort_index туза: {ace_of_spades.sort_index}, sort_index дамы: {queen_of_hearts.sort_index}")
    
    print(f"\nСравнение кортежей: ('A', '♠') > ('Q', '♥'): {('A', '♠') > ('Q', '♥')}")